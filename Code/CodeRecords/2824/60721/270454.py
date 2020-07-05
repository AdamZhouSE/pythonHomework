n,t,c=map(int,input().split(" "))
lis=list(map(int,input().split(' ')))
count=0
q=True
for i in range(c-1,n):
    for j in range(0,c):
        if(lis[i-j]>t):
            q=False
            break
    if(q==True):
        count+=1
    q=True
print(count)