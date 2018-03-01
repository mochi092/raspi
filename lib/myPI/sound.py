import pygame.mixer
import time
import os

class ras_sound:

    def playMP3(self,filename,loop=1,seconds=10):

        # mixerモジュールの初期化
        pygame.mixer.init()
        # 音楽ファイルの読み込み
        pygame.mixer.music.load(filename)
        # 音楽再生、および再生回数の設定(-1はループ再生)
        pygame.mixer.music.play(loop)

        time.sleep(seconds)
        # 再生の終了
        pygame.mixer.music.stop()

    def playWAV(self,filename):
         os.system("aplay '{}'".format(filename))