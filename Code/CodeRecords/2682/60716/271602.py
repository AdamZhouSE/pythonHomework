ucnum = int(input())
ans = list()
for i in range(ucnum):
    n,l,r = map(int,input().split())
    temp = bin(n)[2:]
    print(temp)
for i in ans:
    print(i)