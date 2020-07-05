n,d=map(int,input().split())
list=[int(i) for i in input().split()]
num=0
for i in range(1,n):
    while list[i]<=list[i-1]:
        list[i]+=d
        num+=1
print(num)