n=int(input())
num=list(input().split(" "))
res=0
for i in range(n):
    num[i]=int(num[i])
for i in range(n-1):
    tem=list(input().split(" "))
    if num[int(tem[0])-1]<0 and num[int(tem[1])-1]<0:
        continue
    if num[int(tem[0])-1]<0 or num[int(tem[1])-1]<0:
        res=0
for i in range(n):
    if num[i]>0:
        res+=num[i]
print(res,end="")