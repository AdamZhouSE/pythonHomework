n=int(input())
tem=[]
for i in range(n):
    num=list(input().split(","))
    for j in range(n):
        num[j]=int(num[j])
        tem.append(num[j])
tem.sort()
t=int(input())
print(tem[t-1])