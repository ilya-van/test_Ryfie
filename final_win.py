from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class SecondWindow(QWidget):
    def __init__(self, *args, **qwargs):
        super().__init__(*args, **qwargs)
        self.initUI()
    def initUI(self):
        self.main_layout = QVBoxLayout()

        self.name_lable=QLabel('Тут будет ФИО')
        self.index_label = QLabel('Тут будет индекс Руфье')
        self.resylt_lable = QLabel('Тут будет работоспособность сердца(н,с,в')

        self.main_layout.addWidget(self.name_lable, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.index_label, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.resylt_lable, alignment=Qt.AlignCenter)

        self.setLayout(self.main_layout)



