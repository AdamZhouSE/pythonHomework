a=input().split(' ')
n=int(a[0])
k=int(a[1])
lis = input().split(' ')
lis =[int(i) for i in lis]
res=0
data=[]
for i in range(0,n) :
    if lis[i]<=k:
        data.append(lis[i])
        res+=1
    else:
        break  
for j in range(0,n) :
    if lis[n-j-1]<=k:
        data.append(lis[n-j-1])
        res+=1
    else:
        break  
if res>n:
    print(n)
else:
    
    print(res)
    