n=int(input())
lis=list(map(int,input().split(' ')))
lis.sort()
num=[]
r=0
temp=lis[0]
for i in lis:
    if(temp!=i):
        temp=i
        num.append(r)
    r=r+i
print(lis)
print(max(num))