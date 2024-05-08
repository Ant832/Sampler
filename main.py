from gui import QTGUI
from sounds import DrumKit
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QEventLoop, QTimer
import sys
import threading

class Looper:
    def __init__(self):
        self.cur = (0, 0)
        self.box_rgb = "207, 35, 35"
        self.time_bool = False

        self.drums = DrumKit()

        self.app = QApplication(sys.argv)
        # self.app.aboutToQuit.connect(self.exit_handler)
        self.gui = QTGUI()
        self.gui.show()
        self.button_activation()
        self.add_sounds()
        sys.exit(self.app.exec())

    def exit_handler(self):
        self.set_time_bool()
        sys.exit(self.app.exec())

    def set_time_bool(self):
        if self.gui.start_button.text() == "Start":
            self.gui.start_button.setText("Stop")
        else:
            self.gui.start_button.setText("Start")
        self.time_bool = not(self.time_bool)
        self.loop_grid()
    
    def button_activation(self):
        self.gui.start_button.clicked.connect(self.set_time_bool)
    
    def loop_grid(self):
        while self.time_bool:
            for row in range(4):
                for box in range(4):

                    # current row and box, needs to be saved to restart
                    self.cur = (row, box)
                    current_box = self.gui.rows[self.cur[0]].itemAt(self.cur[1]).widget()
                    # turns on red
                    if self.time_bool:
                        current_box.setStyleSheet(f"background-color: rgb({self.box_rgb})")
                        t1 = threading.Thread(target=self.play_sounds, args=(current_box,))
                        t1.start()
                    
                    # bpm
                    loop = QEventLoop()
                    QTimer.singleShot(250, loop.quit)
                    loop.exec()
                    
                    # turns off red
                    current_box.setStyleSheet(f"background-color: rgb(255, 255, 255)")
    
    def play_sounds(self, current_box):
        if 'kick' in current_box.toPlainText() and 'hihat' in current_box.toPlainText() and 'tom' in current_box.toPlainText():
            self.drums.play_hihat_tom_kick()
        elif 'hihat' in current_box.toPlainText() and 'tom' in current_box.toPlainText():
            self.drums.play_hihat_tom()
        elif 'kick' in current_box.toPlainText() and 'tom' in current_box.toPlainText():
            self.drums.play_kick_tom()
        elif 'kick' in current_box.toPlainText() and 'hihat' in current_box.toPlainText():
            self.drums.play_kick_hihat()
        elif 'kick' in current_box.toPlainText():
            self.drums.play_kick()
        elif 'hihat' in current_box.toPlainText():
            self.drums.play_hihat()
        elif 'tom' in current_box.toPlainText():
            self.drums.play_tom()

    def add_sounds(self):
        self.gui.rows[0].itemAt(0).widget().setText("kick")
        self.gui.rows[1].itemAt(0).widget().setText("kick")
        self.gui.rows[2].itemAt(0).widget().setText("kick")
        self.gui.rows[3].itemAt(0).widget().setText("kick")

        self.gui.rows[0].itemAt(3).widget().setText("hihattom")
        self.gui.rows[1].itemAt(3).widget().setText("hihat")
        self.gui.rows[2].itemAt(3).widget().setText("hihattom")
        self.gui.rows[3].itemAt(3).widget().setText("hihat")

        self.gui.rows[1].itemAt(1).widget().setText("kickhihat")
        self.gui.rows[3].itemAt(1).widget().setText("kickhihat")

        self.gui.rows[0].itemAt(1).widget().setText("tom")
        self.gui.rows[0].itemAt(2).widget().setText("tom")
        self.gui.rows[2].itemAt(1).widget().setText("tom")
        self.gui.rows[2].itemAt(2).widget().setText("tom")


def main():
    _ = Looper()
    

if __name__ == "__main__":
    main()
