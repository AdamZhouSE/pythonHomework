a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int,input().split()))
    for j in range(b):
        if j not in c:
            print(j)