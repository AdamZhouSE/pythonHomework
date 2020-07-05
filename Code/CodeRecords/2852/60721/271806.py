n=int(input())
lis=list(map(int,input().split(' ')))
count=0
temp=lis[0]
a=[]
for i in lis:
    if(i!=temp):
        a.append(count)
        temp=i
        count=0
    count+=1
a.append(count)
num=[]
for i in range(1,len(a)):    
    num.append(2*min(a[i-1],a[i]))
print(max(num))