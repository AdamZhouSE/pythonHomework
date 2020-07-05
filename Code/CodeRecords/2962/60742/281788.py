n,p = [int(i) for i in input().split()]
a = input().split()
res = []
posTaken = []
for t in a:
    num = (ord(t[-3])-ord('A'))*32*32 + (ord(t[-2])-ord('A'))*32 + (ord(t[-1])-ord('A'))
    position = num%p
    if position not in posTaken:
        res.append(position)
        posTaken.append(position)
    else:
        i = 1
        while position in posTaken:
            tmp = (position+i**2)%p
            if tmp not in posTaken:
                position = tmp
                res.append(position)
                posTaken.append(position)
                break
            tmp = (position-i**2)%p
            if tmp not in posTaken:
                position = tmp
                res.append(position)
                posTaken.append(position)
                break
            i += 1
for i in range(len(res)):
    res[i] = str(res[i])
print(' '.join(res))