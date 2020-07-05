listIn = input().split(",")
number = [int(i) for i in listIn]
number.sort()
pairs = [[number[0]]]
length = len(number)
for i in range(1, length):
    find = False
    for l in pairs:
        if number[i] % l[len(l)-1] == 0:
            l.append(number[i])
            find = True
            break
    if not find:
        pairs.append([number[i]])
if len(pairs) == 1:
    print(pairs[0])
else:
    index = 0
    maxL = len(pairs[0])
    for i in range(1, len(pairs)):
        if len(pairs[i]) > maxL:
            index = i
            maxL = len(pairs[i])
    print(pairs[index])