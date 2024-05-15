import sounddevice as sd
from scipy.io.wavfile import write
import os
import wavio as wv


class RecSample:
    def __init__(self):
        self.__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.fs = 44100  # Sample rate
        # self.fs = 22050  # Sample rate
        self.seconds = 0.1  # Duration of recording

    def recording(self):
        myrecording = sd.rec(int(self.seconds * self.fs), samplerate=self.fs, channels=2)
        sd.wait()  # Wait until recording is finished
        write(f'{self.__location__}/output.wav', self.fs, myrecording)  # Save as WAV file
        wv.write(f'{self.__location__}/output.wav', myrecording, self.fs, sampwidth=2)
