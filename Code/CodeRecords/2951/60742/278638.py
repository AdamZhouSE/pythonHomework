s2 = [int(i) for i in list(input())[::-1]]
s3 = [int(i) for i in list(input())[::-1]]
l2 = []
l3 = []
for i in range(len(s2)):
    s2[i] = 1-s2[i]
    base = 1
    num = 0
    for j in range(len(s2)):
        num += base*s2[j]
        base *= 2
    l2.append(num)
    s2[i] = 1-s2[i]
for i in range(len(s3)):
    bits = [0,1,2]
    realBit = s3[i]
    bits.remove(realBit)
    for j in bits:
        s3[i] = j
        base = 1
        num = 0
        for j in range(len(s3)):
            num += base*s3[j]
            base *= 3
        l3.append(num)
    s3[i] = realBit
for i in l2:
    if i in l3:
        print(i,end='')
        break