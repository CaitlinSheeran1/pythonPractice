'''
Caitlin Sheeran
01/15/2025
Introduction PyQt5 Practice
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(1000, 400, 500, 500)
        self.setWindowIcon(QIcon("picture.jpg"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Anton", 40))
        label.setGeometry(0,0, 500, 100)
        label.setStyleSheet("color: #292929;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "text-decoration: underline;")
        label.setAlignment(Qt.AlignCenter | Qt.AlignBottom)

        label2 = QLabel(self)
        label2.setGeometry(130,150, 250, 250)
        pixmap = QPixmap("picture.jpg")
        label2.setPixmap(pixmap)

        label2.setScaledContents(True)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)
        label6 = QLabel("#6", self)
        label7 = QLabel("#7", self)

        label3.setStyleSheet("background-color: red")
        label4.setStyleSheet("background-color: yellow")
        label5.setStyleSheet("background-color: green")
        label6.setStyleSheet("background-color: purple")
        label7.setStyleSheet("background-color: black")

        vbox = QVBoxLayout()
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)
        vbox.addWidget(label6)
        vbox.addWidget(label7)

        central_widget.setLayout(vbox)

        self.button = QPushButton("Click me!", self)
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        print("Button clicked!")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)
        




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()