import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMainWindow, QAction, qApp, QDesktopWidget, QGroupBox, \
    QGridLayout, QPushButton, QVBoxLayout
import tkinter as tk
from tkinter import filedialog


class GUI(QMainWindow):

    def __init__(self, d_width, d_height):
        super(GUI, self).__init__()

        menu = self.menuBar()

        file = menu.addMenu('File')
        size = menu.addMenu('Size')

        # Creation of the functions
        open_function = QAction('Open', self)
        open_function.setShortcut('Ctrl+O')

        close_function = QAction('Close', self)
        close_function.setShortcut('Ctrl+Q')

        save_graph_function = QAction('Save Graph', self)
        save_graph_function.setShortcut('Ctrl+G')

        save_file_function = QAction('Save File', self)
        save_file_function.setShortcut('Ctrl+S')

        # Add options to menu
        file.addAction(open_function)
        file.addAction(save_file_function)
        file.addAction(save_graph_function)
        file.addAction(close_function)

        # Events
        open_function.triggered.connect(self.open_file_function)
        save_graph_function.triggered.connect(self.open_file_function)
        close_function.triggered.connect(self.close_app_function)

        self.resize(d_width*.78, d_height*.75)
        self.init_ui()

    def open_file_function(self):
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename()

    def close_app_function(self):
        qApp.quit()

    def init_ui(self):

        self.add_grid()

        self.setWindowTitle('Automata')

        self.show()

    def add_grid(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
        self.lbHeading1 = QtWidgets.QLabel('You can open a file from "File" menu or by using Ctrl + O command!')
        layout.addWidget(self.lbHeading1, 0, 0)
        self.horizontalGroupBox.setLayout(layout)
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setCentralWidget(windowLayout)

app = QtWidgets.QApplication(sys.argv)
screen_resolution = app.desktop().screenGeometry()
width, height = screen_resolution.width(), screen_resolution.height()
main_GUI = GUI(width, height)
sys.exit(app.exec_())