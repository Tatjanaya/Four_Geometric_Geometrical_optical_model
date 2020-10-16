import sys
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QCoreApplication
import demo
import PyQt5_stylesheets
import warnings

warnings.filterwarnings('ignore')

if __name__ == '__main__':
    isExists = os.path.exists("./datas")
    if not isExists:
        os.mkdir("./datas")
    if not isExists:
        os.mkdir("./img")
    app = QApplication(sys.argv)
    app.setStyleSheet(PyQt5_stylesheets.load_stylesheet_pyqt5(style="style_DarkOrange"))
    MainWindow = QMainWindow()
    ui = demo.MyMainForm()
    ui.show()
    #ui2 = second.NewWindow()
    #ui2.show()
    sys.exit(app.exec_())