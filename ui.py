import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                             QMessageBox, QPlainTextEdit, QHBoxLayout,
                             QLineEdit, QComboBox)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.btn1 = QPushButton('Message', self)
        # self.btn1.clicked.connect(self.activateMessage)

        self.btn2 = QPushButton('Clear', self)
        # self.btn2.clicked.connect(self.clearMessage)
        
        # 라인 에디트 문자열 배치 설정
        self.le1 = QLineEdit('0', self)
        self.le1.setAlignment(QtCore.Qt.AlignRight)

        self.le2 = QLineEdit('0', self)
        self.le2.setAlignment(QtCore.Qt.AlignRight)

        # 콤보 박스 항목 추가 (연산자로 사용)
        self.cb = QComboBox(self)
        self.cb.addItems(['+', '-', '*', '/'])

        # 새로 정의한 위젯을 QHBoxLayout에 배치
        hbox_formular = QHBoxLayout()
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)


        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox_formular) # hbox_formular 배치
        vbox.addLayout(hbox)
        # vbox.addWidget(self.btn1)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon('icon.jfif'))
        self.resize(256, 256)
        self.show()

    def activateMessage(self, text):
        # QMessageBox.information(self, "information", "Button Clicked")
        self.te1.appendPlainText(text)
    
    def clearMessage(self):
        self.te1.clear()