from pydub import AudioSegment
from pydub.playback import play


class DrumKit:
    def __init__(self):
        self.sounds = ['kick', 'hihat']
        self.silence = AudioSegment.from_wav('C:\\Users\\antny\\ProgrammingProjects\\sampler\\silence.wav')
        self.hihat = AudioSegment.from_wav('C:\\Users\\antny\\ProgrammingProjects\\sampler\\hihat.wav')
        self.kick = AudioSegment.from_wav('C:\\Users\\antny\\ProgrammingProjects\\sampler\\kick.wav')
        self.tom = AudioSegment.from_wav('C:\\Users\\antny\\ProgrammingProjects\\sampler\\tom.wav')
    
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

# drums = DrumKit()
# drums.play_kick_hihat()
# silence = AudioSegment.from_wav('C:\\Users\\antny\\ProgrammingProjects\\sampler\\silence.wav')
# hihat = AudioSegment.from_wav('C:\\Users\\antny\\ProgrammingProjects\\sampler\\hihat.wav')
# kick = AudioSegment.from_wav('C:\\Users\\antny\\ProgrammingProjects\\sampler\\kick.wav')
# hihat_loop = silence.overlay(hihat, times=0)

# for i in range(32):
#     hihat_loop = hihat_loop.overlay(hihat, position=i*250)

# kick_loop = hihat_loop.overlay(kick, times=0)
# for i in range(8):
#     kick_loop = kick_loop.overlay(kick, position=i*1000)


# start = time.time()
# for _ in range(4):
#     # play(silence)
#     pass

# end = time.time()
# time_len = end - start
# print(time_len)
