a = int(input())
for i in range(a):
    b, c = map(int, input().split())
    a1 = []
    a2 = []
    sum = 0
    for j in range(b):
        d = list(input().split())
        for k in d:
            a1.append(int(k))
    for j in range(b):
        d = list(input().split())
        for k in d:
            a2.append(int(k))
    for j in a1:
        for k in a2:
            if j+k == c:
                sum += 1
    print(sum)
