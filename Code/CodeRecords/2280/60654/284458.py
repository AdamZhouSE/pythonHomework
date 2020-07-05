a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int,input().split()))
    for j in range(1,b+1):
        if j not in c:
            print(j)