n=int(input())
lis1=list(map(int,input().split(" ")))
lis2=list(map(int,input().split(" ")))
lis2=sorted(lis2)
a=lis2[0]
b=lis2[1]
sum=0
for i in lis1:
    sum+=i
temp1=0
temp2=0
for i in range(a-1,b-1):
    temp1+=lis1[i]
temp2=sum-temp1
print(temp1 if temp1<temp2 else temp2)