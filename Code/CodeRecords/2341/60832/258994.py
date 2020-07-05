All = int(input())

for q in range(0, All):
    temp = input().split()
    x = int(temp[0])
    y = int(temp[1])

    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    for i in range(x):
        if p[i] > q[0]:
            temp = p[i]
            p[i] = q[0]
            q[0] = temp
        q.sort()

    for x in p:
        print(x, end=" ")
    for x in q:
        print(x, end=" ")
    print()
