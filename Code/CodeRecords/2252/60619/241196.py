def canfind(sus, tar):
    listsus = list(sus)
    listtar = list(tar)
    result = True
    for i in range(len(sus)):
        if listsus[i] in listtar:
            del (listtar[listtar.index(listsus[i])])
        else:
            result = False
            break
    return result


t = int(input())
for index in range(t):
    word = input()
    target = input()
    length = len(target)
    position = 0
    counts = 0
    while position < len(word):
        if word[position] in target:
            suspect = word[position: position + length]
            if canfind(suspect, target):
                counts += 1
                position += length
            else:
                position += 1
        else:
            position += 1
    print(counts)
    print(word +" "+ target)
