n=int(input())
x=input()
lis=list(map(int,x.split(" ")))
count=[]
temp=0
for i in range(0,len(lis)):
    if lis[i]==1:
        count.append(temp)
        temp=0
    else:
        temp=temp+1
num=0
for i in lis:
    if i==1:
        num+=1
if num==len(lis):
    print(len(lis)-1)
else:
    print(num+max(count))