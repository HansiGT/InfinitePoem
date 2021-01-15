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

second = []

first_text = ["Bin ich", "Bin ich", "Bin ich", "Bin ich aus", "Bin ich aus", "Bin ich aus", "Bin ich Mensch",
              "Eine Maschine aus Menschen ist", "Ich bin", "Ich bin", "Ich bin", "Ich bin",
              "Ich bin aus", "Ich bin aus", "Ich bin aus mir", "Ich bin aus mir", "Ich bin eine",
              "Ich bin eine",
              "Ich bin eine", "Ich bin eine", "Ich bin eine", "Ich bin meine", "Ich bin meine", "Ich bin meine",
              "Ich bin meine Maschine", "Ich bin meine Maschine", "Ich bin meine Maschine",
              "Ich bin meine Maschine",
              "Ich bin meine Maschine", "Ich bin mein Mensch", "Ich bin mir", "Ich bin mir", "Ich bin mir",
              "Ich bin mir", "Ich bin mir", "Ich bin mir", "Ich bin mir eine", "Ich bin mir eine",
              "Ich bin mir eine",
              "Ich bin mir eine", "Ich bin mir meine", "Ich bin mir meine", "Ich bin mir meine",
              "Ich bin mir meine eigene Maschine", "Ich bin mir meine eigene Maschine",
              "Ich bin mir meine Maschine",
              "Ich bin mir meine Maschine", "Ich bin mir meine Maschine", "Ich bin mir meine Maschine", "Ist",
              "Ist",
              "Ist", "Ist", "Ist", "Ist ein", "Ist ein", "Ist eine", "Ist eine", "Ist mir", "Ist mir",
              "Ist mir",
              "Ich bin eine Maschine", "Ich bin eine Maschine", "Ich bin eine Maschine",
              "Ich bin eine Maschine",
              "Ich bin eine Maschine", "Ich bin eine Maschine", "Maschine aus Linien ist",
              "Maschine aus Linien ist",
              "Maschine aus Menschen ist", "Maschine aus Menschen ist", "Mensch aus Linien ist",
              "Mensch aus Maschinen ist", "Mensch aus Maschinen ist", "Gott"]

second_text = [" aus", " aus", " aus", " aus", " aus mir", " aus mir", " aus mir", " aus mir",
               " aus mir heraus",
               " aus mir heraus", " aus mir heraus", ", der gegen Maschinen kämpft", " eine Linie",
               " eine Linie",
               " eine Linie", " eine Maschine", " eine Maschine", " eine Maschine", " eine Menschenlinie",
               " eine Menschenlinie", " eine Menschenlinie", " eine Schiene", " eine Schiene", " eine Schiene",
               " gegen", " gegen", " gegen", " gegen", " gegen mich", " gegen mich", " gegen mich",
               " gegen mich",
               " heraus", " heraus", " heraus", " heraus", " heraus aus mir", " heraus aus mir",
               " heraus aus mir",
               " heraus aus mir heraus", " heraus aus mir heraus", " heraus aus mir heraus", " ich", " ich",
               " ich",
               " ich", " ich", " ich im Kampf gegen", " ich im Kampf gegen",
               " ich im Kampf gegen meine eigene Maschine",
               " ich im Kampf gegen meine eigene Maschine", " ich im Kampf gegen mich",
               " ich im Kampf gegen mich",
               " im Kampf gegen", " im Kampf gegen", " im Kampf gegen", " Linie aus Maschine aus Mensch",
               " Linie aus Mensch aus Maschine", " Maschine", " Maschine", " Maschine", " Maschine",
               " Maschine",
               " Maschine", " Maschine", " Maschine aus Mensch heraus", " Maschine aus Mensch heraus",
               " Maschine gegen Mensch", " Maschine gegen Mensch", " Maschinenkampf", " Maschinenkampf",
               " Maschinenmensch", " Maschinenmensch", " Maschinenmensch", " Maschinenmensch", " meine",
               " meine",
               " meine", " meine eigene", " meine eigene", " meine eigene", " meine eigene",
               " meine eigene Maschine",
               " meine eigene Maschine", " meine Linie", " meine Linie", " meine Maschine", " meine Maschine",
               " meine Maschine", " meine Maschine", " meine Schiene", " Mensch", " Mensch", " Mensch",
               " Mensch aus Linien", " Mensch aus Linien", " Mensch aus Maschine heraus",
               " Mensch aus Mensch heraus",
               " Mensch, der gegen Maschinen kämpft", " Mensch, der gegen Maschinen kämpft", " Menschenlinie",
               " Menschenlinie", " Menschenlinie", " Mensch gegen Maschine", " Mensch gegen Maschine",
               " Mensch gegen Mensch", " Mensch gegen Mensch", " mir", " mir", " mir", " mir", " mir mein",
               " mir mein",
               " mir meine eigene", " mir meine eigene", " mir meine eigene", " mir meine eigene",
               " mir mein eigen",
               " mir meine Maschine", " mir meine Maschine", " mir meine Maschine", " nur", " nur", " nur",
               " nur ein Mensch", " nur ein Mensch", " nur ein Mensch", " oder nur", " oder nur", " oder nur",
               " oder nur", " oder nur", " oder nur eine Maschine", " oder nur eine Maschine",
               " oder nur eine Menschmaschine", " oder nur eine Menschmaschine",
               " oder nur ein Maschinenmensch",
               " oder nur ein Maschinenmensch", " oder nur ein Mensch", " oder nur ein Mensch",
               " oder nur Maschine", " oder nur Maschine", " oder nur Mensch", " oder nur Mensch", " Schiene",
               " Schiene", " Schiene"]

for (dirpath, dirnames, filenames) in os.walk("tracks/first/"):
    for filename in filenames:
        filepath = dirpath + '/' + filename
        first.append(pygame.mixer.Sound(filepath))

for (dirpath, dirnames, filenames) in os.walk("tracks/second/"):
    for filename in filenames:
        filepath = dirpath + '/' + filename
        second.append(pygame.mixer.Sound(filepath))


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

    p.playAndPrint(0, first[i], first_text[i])
    print(first_text[i])
    pygame.time.wait(int(round(first[i].get_length(), 3) * 1000) + 300)
    if m == 0:
        pygame.time.wait(500)
        for a in range(0, randint(1, 3)):
            p.playAndPrint(0, first[i], ", " + first_text[i])
            print(first_text[i])
            pygame.time.wait(int(round(first[i].get_length(), 3) * 1000) + 300)
    p.playAndPrint(0, second[j], second_text[j])
    print(second_text[j])
    pygame.time.wait(int(round(second[j].get_length(), 3) * 1000) + 300)
    if n == 0:
        pygame.time.wait(750)
        for a in range(0, randint(1, 3)):
            p.playAndPrint(0, second[j], second_text[j])
            print(second_text[j])
            pygame.time.wait(int(round(second[j].get_length(), 3) * 1000) + 300)

    while k > 0:
        j = randint(0, len(second) - 1)
        p.playAndPrint(0, second[j], second_text[j])
        print(second_text[j])
        pygame.time.wait(int(round(second[j].get_length(), 3) * 1000) + 300)
        k = randint(0, 2)
        if l == 0:
            for a in range(0, randint(1, 6)):
                p.playAndPrint(0, second[j], second_text[j])
                print(second_text[j])
                pygame.time.wait(int(round(second[j].get_length(), 3) * 1000) + 300)
        l = randint(0, 19)

    p.letterCount = 0
    print(p.letterCount)
    printer(bytes(" " + os.linesep + os.linesep, "utf-8"))
    pygame.time.wait(1000)
