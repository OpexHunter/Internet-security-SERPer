from googlesearch import search

query = "Сколько стоят бананы"

for i in search(query, tld="co.in", num=100, stop=100, pause=0.1):
    print(i)