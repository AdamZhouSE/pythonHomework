times = int(input())

for i in range(0, times):
    name = input()
    name = name.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
    name = list(name)
    count = 0

    indexOutter = 0
    while indexOutter < len(name):
        tempCharForCmp = name[indexOutter]
        indexInner = indexOutter + 1
        while indexInner < len(name):
            if name[indexInner] == tempCharForCmp:
                del name[indexInner]
                indexInner -= 1
            indexInner += 1
        indexOutter += 1

    if len(name) % 2 == 0:
        print("SHE!")
    else:
        print("HE!")