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
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

        temp_dir = os.path.join(__location__, 'tmpSounds')
        tempfile.tempdir = temp_dir

        self.sounds = ['kick', 'hihat', 'tom', 'output']
        self.silence = AudioSegment.from_wav(os.path.join(f"{__location__}/sound_files", 'silence.wav'))
        self.hihat = AudioSegment.from_wav(os.path.join(f"{__location__}/sound_files", 'hihat.wav'))
        self.kick = AudioSegment.from_wav(os.path.join(f"{__location__}/sound_files", 'kick.wav'))
        self.tom = AudioSegment.from_wav(os.path.join(f"{__location__}/sound_files", 'tom.wav'))
        self.output = AudioSegment.from_wav(os.path.join(f"{__location__}/sound_files", 'output.wav'))
        self.sound_dict = {'kick': self.kick, 'hihat': self.hihat, \
                           'tom': self.tom, 'output': self.output}

    def create_sound(self, sounds):
        """
        Overlays each sound passed from sounds
        Plays created sound
        """
        main_sound = self.sound_dict[sounds[0]]
        for sound in range(1, len(sounds)):
            main_sound = main_sound.overlay(self.sound_dict[sounds[sound]])
        play(main_sound)


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
