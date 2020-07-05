# 12
n = int(input())
for i in range(n):
    input()
    num = input().split()
    for i in range(len(num)):
        num[i] = int(num[i])
    o = []
    e = []
    for i in range(len(num)):
        if num[i]%2 == 0:
            e.append(num[i])
        else:
            o.append(num[i])
    l = e + o
    print(' '.join(str(i) for i in l) + ' ')