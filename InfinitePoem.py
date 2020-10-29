import os
import pygame
from random import randint

pygame.mixer.init()
pygame.init()

pygame.mixer.set_num_channels(10)

first = []

second = []

for (dirpath, dirnames, filenames) in os.walk("tracks/first/"):
    for filename in filenames:
        filepath = dirpath + '/' + filename
        first.append(pygame.mixer.Sound(filepath))

for (dirpath, dirnames, filenames) in os.walk("tracks/second/"):
    for filename in filenames:
        filepath = dirpath + '/' + filename
        second.append(pygame.mixer.Sound(filepath))


def play(channel, track):
    pygame.mixer.Channel(channel).play(track, loops=0)


while True:
    i = randint(0, len(first) - 1)
    j = randint(0, len(second) - 1)
    k = randint(0, 2)
    l = randint(0, 19)
    m = randint(0, 19)
    n = randint(0, 19)

    play(0, first[i])
    pygame.time.wait(int(round(first[i].get_length(), 3) * 1000) + 300)
    if True:
        pygame.time.wait(500)
        for a in range(0, randint(1, 3)):
            play(0, first[i])
            pygame.time.wait(int(round(first[i].get_length(), 3) * 1000) + 300)
    play(0, second[j])
    pygame.time.wait(int(round(second[j].get_length(), 3) * 1000) + 300)
    if n == 0:
        pygame.time.wait(750)
        for a in range(0, randint(1, 3)):
            play(0, second[j])
            pygame.time.wait(int(round(second[j].get_length(), 3) * 1000) + 300)

    while k > 0:
            j = randint(0, len(second) - 1)
            play(0, second[j])
            pygame.time.wait(int(round(second[j].get_length(), 3) * 1000) + 300)
            k = randint(0, 2)
            if l == 0:
                for a in range(0, randint(1, 6)):
                    play(0, second[j])
                    pygame.time.wait(int(round(second[j].get_length(), 3) * 1000) + 300)
            l = randint(0, 19)

    pygame.time.wait(1000)
