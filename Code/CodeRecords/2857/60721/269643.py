n=int(input())
lis=list(map(int,input().split(' ')))
lis.sort()
mi=min(lis)
count=1
q=True
for i in range(2,mi+1):
    for j in range(0,n):
        if(lis[j]%i!=0):
            q=False
            break
    if(q==True):
        count+=1
    q=True    
print(count)