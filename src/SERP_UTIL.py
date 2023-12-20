import pandas as pd
import numpy as np
from collections import Counter
from scipy.spatial.distance import cosine

import os
import sys

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

# Теперь используйте base_path для построения пусbтей к вашим файлам:
path_data = os.path.join(base_path, 'assets/search_data.xlsx')

# Загрузка данных
data = pd.read_excel(path_data)


# Функция для токенизации текста
def tokenize(text):
    return text.lower().split()


# Подсчет частоты слов в документе
def term_frequency(document):
    tf = Counter(document)
    total_count = len(document)
    return {term: freq / total_count for term, freq in tf.items()}


# Подсчет обратной частоты документов для слов в корпусе
def inverse_document_frequency(documents):
    total_docs = len(documents)
    doc_count = Counter()
    for document in documents:
        unique_terms = set(document)
        for term in unique_terms:
            doc_count[term] += 1
    return {term: np.log(total_docs / freq) for term, freq in doc_count.items()}


# Подсчет TF-IDF для корпуса документов
def calculate_tfidf(corpus):
    documents = [tokenize(doc) for doc in corpus]

    idf = inverse_document_frequency(documents)
    tfidfs = []

    for document in documents:
        tf = term_frequency(document)
        tfidfs.append({term: tf_val * idf[term] for term, tf_val in tf.items()})

    return tfidfs


# Функция для вычисления косинусного сходства
def cosine_similarity(doc_features, query_features):
    unique_terms = set(doc_features) | set(query_features)
    doc_vector = np.array([doc_features.get(term, 0) for term in unique_terms])
    query_vector = np.array([query_features.get(term, 0) for term in unique_terms])

    return 1 - cosine(doc_vector, query_vector)


# Обработка текстов статей и подсчет TF-IDF
corpus = data['Статья'].apply(str.lower).tolist()
tfidfs = calculate_tfidf(corpus)
data['TF-IDF'] = tfidfs


# Функция поиска статей
def SERP(query):
    # Токенизация запроса
    tokenized_query = tokenize(query)

    # Подсчет TF-IDF для запроса
    query_tfidf = term_frequency(tokenized_query)
    query_tfidf = {term: query_tfidf.get(term, 0) *
                         np.log(len(corpus) / sum(term in doc for doc in corpus))
                   for term in query_tfidf}

    # Вычисление косинусного сходства
    similarities = [cosine_similarity(doc, query_tfidf) for doc in data['TF-IDF']]

    # Получение индексов по убыванию сходства
    # Возвращаем названия статей и ссылки для топ совпадений
    best_indices = np.argsort(similarities)[::-1]
    results = [(data.iloc[i]['Статья'], data.iloc[i]['Источник']) for i in best_indices if similarities[i] > 0]

    return results