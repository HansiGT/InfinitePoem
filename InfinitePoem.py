import os
import pygame
import win32print
from random import randint

printer_name = win32print.GetDefaultPrinter()


def printer(raw_data):
    hPrinter = win32print.OpenPrinter(printer_name)
    hJob = win32print.StartDocPrinter(hPrinter, 1, ("test of raw data", None, "RAW"))
    win32print.StartPagePrinter(hPrinter)
    win32print.WritePrinter(hPrinter, raw_data)
    win32print.EndPagePrinter(hPrinter)
    win32print.EndDocPrinter(hPrinter)
    win32print.ClosePrinter(hPrinter)


pygame.mixer.init()
pygame.init()
pygame.mixer.set_num_channels(10)

first = []

first_text = next(os.walk("tracks/first/"))[1]

second = []

second_text = next(os.walk("tracks/second/"))[1]

i = 0

for (dirpath, dirnames, filenames) in os.walk("tracks/first/", topdown=False):
    first.append([])
    for filename in filenames:
        first[i].append(pygame.mixer.Sound(dirpath + "/" + filename))

    if len(first[i]) == 0:
        del first[i]
    i += 1

i = 0

for (dirpath, dirnames, filenames) in os.walk("tracks/second/", topdown=False):
    second.append([])
    for filename in filenames:
        second[i].append(pygame.mixer.Sound(dirpath + "/" + filename))

    if len(second[i]) == 0:
        del second[i]
    i += 1


class Player:
    letterCount = 0

    def playAndPrint(self, channel, track, text):
        pygame.mixer.Channel(channel).play(track, loops=0)

        if self.letterCount + len(text) <= 72:
            self.letterCount += len(text)
            printer(bytes(" " + text, "utf-8"))
        else:
            self.letterCount = len(text)
            printer(bytes(" " + os.linesep + text, "utf-8"))
        print(self.letterCount)


printer(bytes(" ", "utf8"))
p = Player()
while True:
    i = randint(0, len(first) - 1)
    j = randint(0, len(second) - 1)
    k = randint(0, 2)
    l = randint(0, 19)
    m = randint(0, 19)
    n = randint(0, 19)

    o = randint(0, len(first[i]) - 1)

    p.playAndPrint(0, first[i][o], first_text[i])
    print(first_text[i])
    pygame.time.wait(int(round(first[i][o].get_length(), 3) * 1000) + 300)
    if m == 0:
        pygame.time.wait(500)
        for a in range(0, randint(1, 3)):
            p.playAndPrint(0, first[i][o], ", " + first_text[i])
            print(", " + first_text[i])
            pygame.time.wait(int(round(first[i][o].get_length(), 3) * 1000) + 300)
    o = randint(0, len(second[j]) - 1)
    p.playAndPrint(0, second[j][o], " " + second_text[j])
    print(" " + second_text[j])
    pygame.time.wait(int(round(second[j][o].get_length(), 3) * 1000) + 300)
    if n == 0:
        pygame.time.wait(750)
        for a in range(0, randint(1, 3)):
            p.playAndPrint(0, second[j][o], ", " + second_text[j])
            print(", " + second_text[j])
            pygame.time.wait(int(round(second[j][o].get_length(), 3) * 1000) + 300)

    while k > 0:
        j = randint(0, len(second) - 1)
        o = randint(0, len(second[j]) - 1)
        p.playAndPrint(0, second[j][o], " " + second_text[j])
        print(" " + second_text[j])
        pygame.time.wait(int(round(second[j][o].get_length(), 3) * 1000) + 300)
        k = randint(0, 2)
        if l == 0:
            for a in range(0, randint(1, 6)):
                p.playAndPrint(0, second[j][o], ", " + second_text[j])
                print(", " + second_text[j])
                pygame.time.wait(int(round(second[j][o].get_length(), 3) * 1000) + 300)
        l = randint(0, 19)

    p.letterCount = 0
    print(p.letterCount)
    printer(bytes(" " + os.linesep + os.linesep, "utf-8"))
    pygame.time.wait(1000)
