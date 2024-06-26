"""
Class and interface for DrumKit sounds
"""

import os
import sys
import tempfile
import array
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
import matplotlib.pyplot as plt 

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


class DrumKit:
    """
    Instances of sounds stored here
    Function for overlaying and playing sounds
    """
    def __init__(self):
        self.__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

        temp_dir = os.path.join(self.__location__, 'tmpSounds')
        tempfile.tempdir = temp_dir

        self.sound_counter = 0
        self.sounds = ['kick', 'hihat', 'tom', 'output']
        self.silence = AudioSegment.from_wav(os.path.join(f"{self.__location__}/sound_files", 'silence.wav'))
        self.hihat = AudioSegment.from_wav(os.path.join(f"{self.__location__}/sound_files", 'hihat.wav'))
        self.kick = AudioSegment.from_wav(os.path.join(f"{self.__location__}/sound_files", 'kick.wav'))
        self.tom = AudioSegment.from_wav(os.path.join(f"{self.__location__}/sound_files", 'tom.wav'))
        self.output0 = None
        self.sound_dict = {'kick': self.kick, 'hihat': self.hihat, \
                           'tom': self.tom}
        self.recorded_sounds = []
        self.update_sound_dict(None)

    def create_sound(self, sounds):
        """
        Overlays each sound passed from sounds
        Plays created sound
        """
        main_sound = self.sound_dict[sounds[0]]
        for sound in range(1, len(sounds)):
            main_sound = main_sound.overlay(self.sound_dict[sounds[sound]])
        play(main_sound)
    
    def create_sample(self):
        self.recorded_sounds.append(AudioSegment.from_wav(os.path.join(f"{self.__location__}\\sound_files", f"output{self.sound_counter}.wav")))
        self.sound_dict[f"output{self.sound_counter}"] = self.recorded_sounds[self.sound_counter]
        self.update_sound_dict(f"output{self.sound_counter}")
    
    def update_sound_dict(self, new):
        if new is not None:
            with open(f"{self.__location__}\\config.ini", "a") as config_file:
                config_file.write(f"\n{new}, self.{new}")
            with open(f"{self.__location__}\\config.ini", "r+") as config_file:
                # config_data = config_file.read()
                config_file.seek(0, 0)
                config_file.write(f"{self.sound_counter}\n")
            self.sound_counter += 1
        elif new is None:
            with open(f"{self.__location__}//config.ini", "r") as config_file:
                lines = config_file.readlines()
                self.sound_counter = int(lines[0])
                for line in range(len(lines)):
                    if line == 0:
                        continue
                    lines[line] = lines[line].split(',')
                    if "output" in lines[line][0] and new:
                        self.sound_dict[lines[line][0]] = self.recorded_sounds[int(lines[line][0][-1])]
                    elif "output" not in lines[line][0]:
                        self.sound_dict[lines[line][0]] = self.sound_dict[lines[line][0]]
                
    def view_sound(self, sound_wave):
        """
        Visualizes sound wave
        """
        show_sound = self.sound_dict[sound_wave]
        samples = show_sound.get_array_of_samples()

        # Example operation on audio data
        shifted_samples = np.right_shift(samples, 1)

        # now you have to convert back to an array.array
        shifted_samples_array = array.array(show_sound.array_type, shifted_samples)

        plt.rcParams['toolbar'] = 'None'
        plt.xticks([])
        plt.yticks([])
        plt.plot(shifted_samples_array)
        plt.show()


def main():
    """
    Interface for testing user recorded sounds
    """
    # new = DrumKit()
    # new.play_output()
    # new.play_hihat_tom()
    # play(AudioSegment.from_wav('C:\\Users\\antny\\ProgrammingProjects\\Sampler\\sound_files\\output0.wav'))

    new = DrumKit()
    new.view_sound()


if __name__ == "__main__":
    main()
