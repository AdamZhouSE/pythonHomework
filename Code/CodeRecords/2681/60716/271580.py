ucnum = int(input())
ans = list()
for i in range(ucnum):
    n = int(input())
    index = 0
    while True:
        index+=1
        if n%2==0:
            n = n//2
        else:
            n-=1
        if n==0:
            break
for i in ans:
    print(i)