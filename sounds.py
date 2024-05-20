"""
Class and interface for DrumKit sounds
"""

import os
import sys
import tempfile
from pydub import AudioSegment
from pydub.playback import play

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
    
    def create_sample(self, num):
        self.recorded_sounds.append(AudioSegment.from_wav(os.path.join(f"{self.__location__}\\sound_files", f"output{num}.wav")))
        self.sound_dict[f"output{num}"] = self.recorded_sounds[num]
        self.update_sound_dict(f"output{num}")
    
    def update_sound_dict(self, new):
        if new:
            with open(f"{self.__location__}\\config.ini", "a") as config_file:
                config_file.write(f"\n{new}, self.{new}")
        with open(f"{self.__location__}\\config.ini", "r") as config_file:
            lines = config_file.readlines()
            for line in lines:
                line = line.split(',')
                if "output" in line[0] and new:
                    self.sound_dict[line[0]] = self.recorded_sounds[int(line[0][-1])]
                elif "output" not in line[0]:
                    self.sound_dict[line[0]] = self.sound_dict[line[0]]
                elif "output" in line[0] and not new:
                    self.create_sample(int(line[0][-1]))


def main():
    """
    Interface for testing user recorded sounds
    """
    # new = DrumKit()
    # new.play_output()
    # new.play_hihat_tom()
    play(AudioSegment.from_wav('C:\\Users\\antny\\ProgrammingProjects\\Sampler\\output.wav'))


if __name__ == "__main__":
    main()
