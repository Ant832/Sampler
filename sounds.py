from pydub import AudioSegment
from pydub.playback import play
import os
import tempfile


class DrumKit:
    def __init__(self):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

        temp_dir = os.path.join(__location__, 'tmpSounds')
        tempfile.tempdir = temp_dir
        
        self.sounds = ['kick', 'hihat', 'tom', 'output']
        self.silence = AudioSegment.from_wav(os.path.join(__location__, 'silence.wav'))
        self.hihat = AudioSegment.from_wav(os.path.join(__location__, 'hihat.wav'))
        self.kick = AudioSegment.from_wav(os.path.join(__location__, 'kick.wav'))
        self.tom = AudioSegment.from_wav(os.path.join(__location__, 'tom.wav'))
        self.output = AudioSegment.from_wav(os.path.join(__location__, 'output.wav'))
        self.sound_dict = {'kick': self.kick, 'hihat': self.hihat, 'tom': self.tom, 'output': self.output}
    
    def create_sound(self, sounds):
        main_sound = self.sound_dict[sounds[0]]
        for sound in range(1, len(sounds)):
            main_sound = main_sound.overlay(self.sound_dict[sounds[sound]])
        play(main_sound)


def main():
    # new = DrumKit()
    # new.play_output()
    # new.play_hihat_tom()
    try:
        play(AudioSegment.from_wav('C:\\Users\\antny\\ProgrammingProjects\\Sampler\\output.wav'))
    except Exception as e:
        print("Error: ", e)
    print('done')


if __name__ == "__main__":
    main()
