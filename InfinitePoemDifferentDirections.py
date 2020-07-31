import os
import pygame
from random import randint

pygame.mixer.init()
pygame.init()

pygame.mixer.set_num_channels(26)

first = []

second = []

for (dirpath, dirnames, filenames) in os.walk("tracks/firstStereo/"):
    for filename in filenames:
        filepath = dirpath + '/' + filename
        first.append(pygame.mixer.Sound(filepath))

for (dirpath, dirnames, filenames) in os.walk("tracks/secondStereo/"):
    for filename in filenames:
        filepath = dirpath + '/' + filename
        second.append(pygame.mixer.Sound(filepath))


def play(x, channel, track):
    pygame.mixer.Channel(channel).play(track, loops=0, maxtime=x)


while True:
    i = randint(0, len(first) - 1)
    j = randint(0, len(second) - 1)
    k = randint(0, 2)
    l = randint(0, 9)

    play(10000, 0, first[i])
    pygame.time.wait(int(round(first[i].get_length(), 3) * 1000) + 300)
    play(10000, 0, second[j])
    pygame.time.wait(int(round(second[j].get_length(), 3) * 1000) + 300)

    if l == 0:
        for a in range(0, 4):
            play(10000, 0, second[j])
            pygame.time.wait(int(round(second[j].get_length(), 3) * 1000) + 300)
    else:
        while k > 0:
            j = randint(0, len(second) - 1)
            play(10000, 0, second[j])
            pygame.time.wait(int(round(second[j].get_length(), 3) * 1000) + 300)
            k = randint(0, 2)

    pygame.time.wait(2000)
