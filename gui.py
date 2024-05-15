from PySide6.QtWidgets import QWidget, QMainWindow, QGridLayout, QTextEdit, QHBoxLayout, QPushButton, QVBoxLayout, QMenu, QMessageBox


class QTGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sampler")
        self.setGeometry(100, 100, 700, 500)
        self.make_grid()
    
    def make_grid(self):
        self.main_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()
        self.button_layout = QHBoxLayout()

        self.make_box()
        self.make_buttons()
        self.create_menu_bar()

        self.main_layout.addLayout(self.grid_layout)
        self.main_layout.addLayout(self.button_layout)

        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)
    
    def make_box(self):
        self.rows = []
        for i in range(4):
            self.row = QHBoxLayout()
            self.rows.append(self.row)
            for _ in range(4):
                self.box = QTextEdit()
                self.box.setStyleSheet("background-color: rgb(255, 255, 255)")
                # self.box.setReadOnly(True)
                self.row.addWidget(self.box)
            self.grid_layout.addLayout(self.row, i, 0)
    
    def make_buttons(self):
        self.start_button = QPushButton()
        self.start_button.setText("Start")

        self.button_layout.addWidget(self.start_button)
    
    def create_menu_bar(self):
        menu_bar = self.menuBar()
        self.record_menu = QMenu("&Record Sample", self)
        menu_bar.addMenu(self.record_menu)
        menu_bar.setStyleSheet(f"background-color: rgb(200, 200, 200);")
