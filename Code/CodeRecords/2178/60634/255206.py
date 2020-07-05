def write(sent, magicBook):
    i = 0
    while i <= len(magicBook):
        if i == len(magicBook):
            magicBook.append(sent)
            return True
        if len(sent) == len(magicBook[i]):
            j = 0
            while j <= len(sent):
                if j == len(sent):
                    return False
                if sent[j] != magicBook[i][j]:
                    break
                j += 1
        i += 1


def buildMagic(magic, magicBook):
    length = len(magic)
    i = length - 1
    while i >= 0:
        write(magic[i:length], magicBook)
        i -= 1


n = int(input())
words = input().split(" ")

magic = []
magicBook = []

i = 0
while i < n:
    magic.append(int(words[i]))
    buildMagic(magic, magicBook)
    print(len(magicBook))
    i += 1