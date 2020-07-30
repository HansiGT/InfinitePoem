
import pygame
from random import randint

pygame.mixer.init()
pygame.init()

pygame.mixer.set_num_channels(26)

tracks = [pygame.mixer.Sound("tracks/Aus.wav"), pygame.mixer.Sound("tracks/AusMir.wav"), pygame.mixer.Sound("tracks/BinIch.wav"),
          pygame.mixer.Sound("tracks/EineMaschine.wav"), pygame.mixer.Sound("tracks/EineMaschineAusSchienenIst.wav"), pygame.mixer.Sound("tracks/EineSchiene.wav"),
          pygame.mixer.Sound("tracks/EineSchienedieMaschineIst.wav"), pygame.mixer.Sound("tracks/Heraus.wav"), pygame.mixer.Sound("tracks/IchBin.wav"),
          pygame.mixer.Sound("tracks/IchBinEineMaschine.wav"), pygame.mixer.Sound("tracks/IchBinMeineMaschine.wav"),
          pygame.mixer.Sound("tracks/IchBinMirMeineMaschine.wav"), pygame.mixer.Sound("tracks/IsstDieMaschineDieSchiene.wav"), pygame.mixer.Sound("tracks/IsstDieSchieneDieMaschine.wav"),
          pygame.mixer.Sound("tracks/IstEineMaschineEineMaschine.wav"), pygame.mixer.Sound("tracks/Maschine.wav"), pygame.mixer.Sound("tracks/Maschinenmensch.wav"),
          pygame.mixer.Sound("tracks/MeineEigeneMaschine.wav"), pygame.mixer.Sound("tracks/MeineEineMaschine.wav"), pygame.mixer.Sound("tracks/MeineMaschine.wav"),
          pygame.mixer.Sound("tracks/MeineSchiene.wav"), pygame.mixer.Sound("tracks/Mir.wav"), pygame.mixer.Sound("tracks/NurEineMaschine.wav"), pygame.mixer.Sound("tracks/OderNurEineMaschine.wav"),
          pygame.mixer.Sound("tracks/Schiene.wav"), pygame.mixer.Sound("tracks/SchieneDieEineMaschineIst.wav")]

first = [pygame.mixer.Sound("tracks/IchBin.wav"), pygame.mixer.Sound("tracks/EineMaschineAusSchienenIst.wav"), pygame.mixer.Sound("tracks/IchBinEineMaschine.wav"),
         pygame.mixer.Sound("tracks/IchBinMeineMaschine.wav"), pygame.mixer.Sound("tracks/IchBinMirMeineMaschine.wav"), pygame.mixer.Sound("tracks/IsstDieMaschineDieSchiene.wav"),
         pygame.mixer.Sound("tracks/IsstDieSchieneDieMaschine.wav"), pygame.mixer.Sound("tracks/IstEineMaschineEineMaschine.wav"), pygame.mixer.Sound("tracks/BinIch.wav"),]


second = [pygame.mixer.Sound("tracks/EineMaschine.wav"), pygame.mixer.Sound("tracks/EineSchiene.wav"), pygame.mixer.Sound("tracks/EineSchienedieMaschineIst.wav"),
         pygame.mixer.Sound("tracks/Maschine.wav"), pygame.mixer.Sound("tracks/Maschinenmensch.wav"), pygame.mixer.Sound("tracks/MeineEigeneMaschine.wav"),
         pygame.mixer.Sound("tracks/MeineEineMaschine.wav"), pygame.mixer.Sound("tracks/MeineMaschine.wav"), pygame.mixer.Sound("tracks/MeineSchiene.wav"),
         pygame.mixer.Sound("tracks/Mir.wav"), pygame.mixer.Sound("tracks/NurEineMaschine.wav"),
         pygame.mixer.Sound("tracks/Schiene.wav"), pygame.mixer.Sound("tracks/SchieneDieEineMaschineIst.wav"), pygame.mixer.Sound("tracks/Heraus.wav"), pygame.mixer.Sound("tracks/Aus.wav"),
         pygame.mixer.Sound("tracks/AusMir.wav"), pygame.mixer.Sound("tracks/OderNurEineMaschine.wav")]



def play(x, channel, track):
    pygame.mixer.Channel(channel).play(track, loops=0, maxtime=x)


def queue(channel, track):
    pygame.mixer.Channel(channel).queue(track)


while True:
    i = randint(0, len(first)-1)
    j = randint(0, len(second)-1)
    k = randint(0, 2)

    play(10000, 0, first[i])
    pygame.time.wait(int(round(first[i].get_length(), 3)*1000) + 300)
    play(10000, 0, second[j])
    pygame.time.wait(int(round(second[j].get_length(), 3) * 1000) + 300)

    while k > 0:
        j = randint(0, len(second) - 1)
        play(10000, 0, second[j])
        pygame.time.wait(int(round(second[j].get_length(), 3) * 1000) + 300)
        k = randint(0, 2)

    pygame.time.wait(2000)
