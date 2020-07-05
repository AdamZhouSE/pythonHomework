inputs = input().strip("[]").split("],[")
blocks = []
for i in inputs:
    i = i.split(",")
    i = list(map(int,i))
    blocks.append(i)
length = len(blocks)
i = 0
while i < length - 1:
    j = i + 1
    while j < length:
        blA = blocks[i]
        blB = blocks[j]
        if (blA[0] <= blB[0])and(blA[1] >= blB[1]):
            blC = [blA[0],blA[1]]
        elif (blA[0] >= blB[0])and(blA[1] <= blB[1]):
            blC = [blB[0],blB[1]]
        elif (blA[0] <= blB[1])and(blA[1] >= blB[1]):
            blC = [blB[0],blA[1]]
        elif (blA[0] <= blB[0])and(blA[1] >= blB[0]):
            blC = [blA[0],blB[1]]
        else:
            j = j + 1
            continue
        blocks.remove(blA)
        blocks.remove(blB)
        blocks.insert(i,blC)
        length = length - 1
    i = i + 1
print(blocks)