import sys
import os
import snake, alien
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)  # Загружаем дизайн
        self.snake_btn.clicked.connect(self.run)
        self.space_btn.clicked.connect(self.runn)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        print('<3')
        snake.start()

    def runn(self):
        print('>3')
        alien.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())