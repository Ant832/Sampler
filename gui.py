"""
GUI setup
"""

from PySide6.QtWidgets import QWidget, QMainWindow, QGridLayout, QTextEdit, QHBoxLayout, QPushButton, QVBoxLayout, QMenu


class QTGUI(QMainWindow):
    """
    Main gui class
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sampler")
        self.setGeometry(100, 100, 700, 500)
        self.start_button = QPushButton()
        self.view_kick = QPushButton()
        self.view_tom = QPushButton()
        self.view_hihat = QPushButton()
        self.record_menu = QMenu("&Record Sample", self)
        self.rows = []
        self.make_grid()

    def make_grid(self):
        """
        QT layouts
        """
        self.main_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()
        self.button_layout = QVBoxLayout()
        self.view_layout = QHBoxLayout()

        self.make_box()
        self.make_buttons()
        self.create_menu_bar()

        self.main_layout.addLayout(self.grid_layout)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addLayout(self.view_layout)

        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def make_box(self):
        """
        Creates grid of 16 boxes
        """
        for i in range(4):
            row = QHBoxLayout()
            self.rows.append(row)
            for _ in range(4):
                box = QTextEdit()
                box.setStyleSheet("background-color: rgb(255, 255, 255)")
                row.addWidget(box)
            self.grid_layout.addLayout(row, i, 0)

    def make_buttons(self):
        """
        Creates buttons on main gui
        """
        self.view_kick.setText("View Kick")
        self.view_tom.setText("View Tom")
        self.view_hihat.setText("View Hihat")
        self.view_layout.addWidget(self.view_kick)
        self.view_layout.addWidget(self.view_tom)
        self.view_layout.addWidget(self.view_hihat)


        self.start_button.setText("Start")
        self.button_layout.addWidget(self.start_button)
        
        

    def create_menu_bar(self):
        """
        Creates menu bar on main gui
        """
        menu_bar = self.menuBar()
        menu_bar.addMenu(self.record_menu)
        menu_bar.setStyleSheet("background-color: rgb(200, 200, 200);")
