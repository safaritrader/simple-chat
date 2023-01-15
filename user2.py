import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import requests

class Window1(QMainWindow):
    def __init__(self):
        super(Window1,self).__init__()
        self.setGeometry(100, 30, 612, 354)
        self.setWindowTitle("Chat")
        self.UI()
    def UI(self):
        self.Send = QPushButton(self)
        self.Send.setGeometry(QRect(530, 260, 77, 23))
        self.Send.setText("Send Message")
        self.Send.clicked.connect(self.messagesend)
        self.Clear = QPushButton(self)
        self.Clear.setGeometry(QRect(510, 310, 101, 23))
        self.Clear.setText("Clear All Message")
        self.Clear.clicked.connect(self.clearmessage)
        self.update = QPushButton(self)
        self.update.setGeometry(QRect(530, 283, 75, 23))
        self.update.setText("Update")
        self.update.clicked.connect(self.Readmessage)

        self.textBrowser = QTextBrowser(self)
        self.textBrowser.setGeometry(QRect(10, 20, 191, 311))
        self.textBrowser_2 = QTextBrowser(self)
        self.textBrowser_2.setGeometry(QRect(200, 20, 191, 311))
        self.label = QLabel(self)
        self.label.setGeometry(QRect(20, 0, 47, 13))
        self.label.setText("User")
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(200, 0, 47, 13))
        self.label_2.setText("User2")
        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(QRect(400, 20, 201, 231))
    def messagesend(self):
        try:
            txt = self.textEdit.toPlainText()
            url = 'http://url/user2/{}'.format(txt)
            resp = requests.get(url=url)
        except Exception:
            print("error")
    def Readmessage(self):
        try:
            url = 'http://url/'
            resp = requests.get(url=url)
            data = resp.json()
            self.textBrowser.setText(data["user1 Message : "])
            self.textBrowser_2.setText(data["user2 Message : "])
        except Exception:
            self.textBrowser.setText("Connection Error")
    def clearmessage(self):
        try:
            url = 'http://URL/user2clearmessage'
            resp = requests.get(url=url)
        except Exception:
            print("error")
def main():
    app = QApplication(sys.argv)
    window = Window1()
    window.show()
    #app.exec()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()