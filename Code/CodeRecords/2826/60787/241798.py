n=int(input())
medal=[int(i) for i in input().split()]
medal=sorted(medal)
num=0
for i in range(1,n):
    while medal[i]<=medal[i-1]:
        medal[i]+=1
        num+=1
print(num)