k = int(input())
numOfEachEp = []
lensOfEachEp = []
for i in range(k):
    n = int(input())
    lens = list(map(int, input().split(' ')))
    numOfEachEp.append(n)
    lensOfEachEp.append(lens)
for i in range(k):
    n = numOfEachEp[i]
    lens = lensOfEachEp[i]
    support = list(range(n))
    support.reverse()
    for x in support:
        x = x + 1
        count = 0
        for l in lens:
            if l >= x:
                count = count + 1
        if count >= x:
            print(x)
            break