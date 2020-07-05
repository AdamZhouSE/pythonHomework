t = int(input())
for i in range(t):
    mnab = list(map(int, input().split()))
    m = mnab[0]
    n = mnab[1]
    a = mnab[2]
    b = mnab[3]
    count = 0
    for j in range(m, n+1):
        if j % a == 0 or j % b == 0:
            count+=1
    print(count)        