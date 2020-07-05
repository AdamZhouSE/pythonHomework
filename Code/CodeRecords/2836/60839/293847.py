n=int(input())
x=input()
lis=list(map(int,x.split(" ")))

count=0
temp=0
for i in range(0,len(lis)-1):
    if lis[i+1]<lis[i]:
        temp=i
        count+=1
if lis[len(lis)-1]>lis[0]:
    count+=1
if count>1:
    print(-1)
elif sorted(lis)==lis:
    print(0)
else:
    print(len(lis)-temp-1)