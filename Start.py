import sys
import os
import threading
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolBar, QLineEdit, QTextEdit,\
    QSplitter, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import G2G, P2P



class Main_UI(QWidget):
    def __init__(self):
        super(Main_UI, self).__init__()
        self.width  = 600                     # MainUI Width 
        self.height = 680                     # MainUI Height
        self.title  = "CHEChannel"            # Title
        self.font   = QFont('Serif', 17)      # General Font
        self.layout = QVBoxLayout(self)       # Main Layout
        self.split  = QSplitter(Qt.Vertical)  # Splitter
        self.bar_1  = QToolBar(self)          # Bar
        self.screen = QTextEdit(self)         # Chat Screen
        self.btn_1  = QPushButton(self)       # Send Button
        self.edt_1  = QLineEdit(self)         # Message Input
        self.Init_UI()
        
        
    def Init_UI(self):
        # Main UI - QMainWindow
        self.setWindowTitle(self.title)
        self.setGeometry(10, 40, self.width, self.height)
        self.setStyleSheet('background-color:#444;')
        self.setLayout(self.layout)
        # Main Layout - QGridBox
        self.layout.addWidget(self.split)
        # Splitter - QSplitter
        self.split.addWidget(self.bar_1)
        self.split.addWidget(self.screen)
        self.split.addWidget(self.edt_1)
        self.split.addWidget(self.btn_1)
        # Bar - QToolBar
        
        # Chat Screen - QTextEdit
        self.screen.setReadOnly(True)
        self.screen.setStyleSheet('background-color:transparent;color:#fff;border:1px solid #bbb;')
        # Message Input - QLineEdit
        self.edt_1.setFocus(True)
        self.edt_1.setFont(self.font)
        self.edt_1.setStyleSheet('background-color:transparent;border:none;border-bottom:2px solid #fff;\color:#fff;height:20px;')
        # Send Burron - QPushButton
        self.btn_1.setText("Send")
        self.btn_1.setFont(self.font)
        self.btn_1.setStyleSheet('background-color:lime;border:none;color:#fff;')
        self.btn_1.clicked.connect(self.Print_Screen)
    
    def Print_Screen(self):
        self.t = self.edt_1.text()
        self.screen.append(self.t)
        

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Obj = Main_UI()
    Obj.show()
    sys.exit(App.exec_())