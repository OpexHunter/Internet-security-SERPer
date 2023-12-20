import sys
import webbrowser
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QHeaderView, QTableWidgetItem, QTableView, \
    QVBoxLayout, QWidget
from setupUI import Ui_MainWindow
from SERP_UTIL_GOOGLE import SERP

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        # Модель данных
        model_clear = QStandardItemModel()
        model_clear.setHorizontalHeaderLabels(['Статья', 'Ссылка'])
        model_clear.appendRow([QStandardItem(""), QStandardItem("")])
        self.ui.SearchView.setModel(model_clear)

        # Размеры столбцов
        self.ui.SearchView.setColumnWidth(0, 570)
        self.ui.SearchView.setColumnWidth(1, 500)
        self.ui.SearchView.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.SearchView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.ui.SearchView.setEditTriggers(QTableView.NoEditTriggers)

        self.ui.b_clear.clicked.connect(lambda: self.ui.SearchView.setModel(model_clear))
        self.ui.b_search.clicked.connect(lambda: self.__Search(self.ui.l_search.text()))

        self.ui.SearchView.clicked.connect(self.click_on_table)

    def click_on_table(self, index):
        # Проверяем, что клик был сделан по второму столбцу (индекс 1)
        if index.column() == 1:
            # Получаем ссылку из модели данных в этой ячейке
            link = self.ui.SearchView.model().item(index.row(), index.column()).text()
            if link:  # Убедитесь, что ссылка не пустая
                webbrowser.open(link)  # Открываем ссылку в браузере

    def __model(self, data):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Статья', 'Ссылка'])
        for title, link in data:
            model.appendRow([QStandardItem(title), QStandardItem(link)])
        if len(data) == 0:
            model.appendRow([QStandardItem('Cтатья не найдена'), QStandardItem('')])
        self.ui.SearchView.setModel(model)


    def __Search(self, data):
        try:
            self.__model(SERP(data))
        except:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(['Статья', 'Ссылка'])
            model.appendRow([QStandardItem('Cтатья не найдена'), QStandardItem('')])
            self.ui.SearchView.setModel(model)
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())