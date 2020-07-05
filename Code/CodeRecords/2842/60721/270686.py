n=int(input())
lis=[]
for i in range(0,n):
    lis.append(int(input()))
num=[]
for i in range(0,n):
    count=0
    if(lis[i]==-1):
        num.append(count+1)
    else:
        a=lis[lis[i]-1]
        count+=1
        while (a!=-1):
            count+=1
            a=lis[lis[a]-1]
        num.append(count+1)
print(max(num))