import os
import pygame
import random
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
    r = random.uniform(0, 1)
    pygame.mixer.Channel(channel).set_volume(r, (1 - r))


while True:
    i = randint(0, len(first) - 1)
    j = randint(0, len(second) - 1)
    k = randint(0, 2)
    l = randint(0, 9)


    play(0, first[i])
    pygame.time.wait(int(round(first[i].get_length(), 3) * 1000) + 300)
    play(0, second[j])
    pygame.time.wait(int(round(second[j].get_length(), 3) * 1000) + 300)

    if l == 0:
        for a in range(0, 4):
            play(0, second[j])
            pygame.time.wait(int(round(second[j].get_length(), 3) * 1000) + 300)
    else:
        while k > 0:
            j = randint(0, len(second) - 1)
            play(0, second[j])
            pygame.time.wait(int(round(second[j].get_length(), 3) * 1000) + 300)
            k = randint(0, 2)

    pygame.time.wait(2000)
