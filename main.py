"""
Main file for running looper
"""

import sys
import threading
from gui import QTGUI
from sounds import DrumKit
from PySide6.QtWidgets import QApplication, QMessageBox, QPushButton
from PySide6.QtCore import QEventLoop, QTimer
from record import RecSample


class Looper:
    """
    Controller class for sounds, recording, and gui
    """
    def __init__(self):
        self.cur = (0, 0)
        self.box_rgb = "207, 35, 35"
        self.time_bool = False

        self.sounds = ["kick", "tom", "hihat"]

        self.drums = DrumKit()
        self.mic_use = RecSample()

        self.app = QApplication(sys.argv)
        # self.app.aboutToQuit.connect(self.exit_handler)
        self.gui = QTGUI()
        self.gui.show()
        self.button_activation()
        self.add_sounds()
        sys.exit(self.app.exec())

    def exit_handler(self):
        """
        Closes program without causing sound errors
        TODO: fix^
        """
        self.set_time_bool()
        sys.exit(self.app.exec())

    def set_time_bool(self):
        """
        Starts and stops looper
        """
        if self.gui.start_button.text() == "Start":
            self.gui.start_button.setText("Stop")
        else:
            self.gui.start_button.setText("Start")
        self.time_bool = not self.time_bool
        self.loop_grid()

    def button_activation(self):
        """
        Button connector
        """
        self.gui.record_menu.addAction("Open Recording Page", self.record_dialog)
        self.gui.start_button.clicked.connect(self.set_time_bool)
        self.gui.view_kick.clicked.connect(lambda: self.drums.view_sound("kick"))
        self.gui.view_tom.clicked.connect(lambda: self.drums.view_sound("tom"))
        self.gui.view_hihat.clicked.connect(lambda: self.drums.view_sound("hihat"))

    def record_dialog(self):
        """
        Menu button for recording sounds
        """
        dialog = QMessageBox()
        record_button = QPushButton()
        record_button.setText("Record")
        dialog.addButton(record_button, dialog.ButtonRole(1))
        dialog.setStyleSheet("background: rgb(200, 200, 200);")
        record_button.clicked.connect(self.start_recording)
        _ = dialog.exec()

    def start_recording(self):
        """
        Uses sounds.py to record audio
        Reinitializes Drumkit to update new user sound
        """
        print(self.drums.sound_counter)
        self.mic_use.recording(self.drums.sound_counter)
        self.drums.sound_counter += 1
        self.drums.create_sample()

    def loop_grid(self):
        """
        Loops over sound grid
        """
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
                    QTimer.singleShot(150, loop.quit)
                    loop.exec()

                    # turns off red
                    current_box.setStyleSheet("background-color: rgb(255, 255, 255)")

    def play_sounds(self, current_box):
        """
        Calls sounds.py fuction to create and play sounds in current_box
        """
        current_sounds = []
        text = current_box.toPlainText()
        for i in range(len(self.sounds)):
            if "output" in text:
                new_output = text[text.index("output"):text.index("output")+7]
                if new_output not in current_sounds:
                    current_sounds.append(new_output)
            if self.sounds[i] in text:
                current_sounds.append(self.sounds[i])
        self.drums.create_sound(current_sounds) # plays sounds

    def add_sounds(self):
        """
        Used for adding sounds to grid on startup
        """
        for i in range(4):
            for j in range(4):
                self.gui.rows[i].itemAt(j).widget().append("hihat")

        self.gui.rows[0].itemAt(0).widget().append("kick")
        self.gui.rows[1].itemAt(0).widget().append("kick")
        self.gui.rows[1].itemAt(1).widget().append("kick")
        self.gui.rows[2].itemAt(1).widget().append("kick")
        self.gui.rows[3].itemAt(0).widget().append("kick")
        self.gui.rows[3].itemAt(1).widget().append("kick")

        for i in range(4):
            self.gui.rows[i].itemAt(2).widget().append("tom")


def main():
    """
    Creates instance of main Looper
    """
    _ = Looper()


if __name__ == "__main__":
    main()
