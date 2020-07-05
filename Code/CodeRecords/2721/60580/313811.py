size = int(input())
a = 0
while a < size:
    l = input().split()
    aT = int(l[0], 2)
    bT = int(l[1], 2)
    result = aT * bT
    print(result)
    a = a + 1