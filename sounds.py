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
    
    def play_output(self):
        play(self.output)
    
    def play_kick(self):
        play(self.kick)

    def play_hihat(self):
        play(self.hihat)
    
    def play_kick_hihat(self):
        kick_hihat = self.kick.overlay(self.hihat)
        play(kick_hihat)

    def play_tom(self):
        play(self.tom)
    
    def play_kick_tom(self):
        kick_tom = self.kick.overlay(self.tom)
        play(kick_tom)
    
    def play_hihat_tom(self):
        hihat_tom = self.hihat.overlay(self.tom)
        play(hihat_tom)

    def play_hihat_tom_kick(self):
        hihat_tom = self.hihat.overlay(self.tom)
        hihat_tom_kick = hihat_tom.overlay(self.kick)
        play(hihat_tom_kick)


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
