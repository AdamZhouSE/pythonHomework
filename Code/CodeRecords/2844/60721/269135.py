n,t=map(int,input().split(' '))
lis=list(map(int,input().split(' ')))
num=[]
for i in range(0,n):
    count=0
    time=0
    for j in range(i,n):
        time+=lis[j]
        if(time<=t):
            count+=1
        else:
            num.append(count)
            break
        if(j==n-1):
            num.append(count) 
print(max(num))