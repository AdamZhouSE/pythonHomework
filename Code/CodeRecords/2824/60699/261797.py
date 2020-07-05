list1=list(map(int,input().split(' ')))
guilty=list(map(int,input().split(' ')))
t=list1[1]
sz=list1[2]
n=list1[0]
res=0
for i in range(0,n-sz+1):
    temp=0
    for j in range(i,i+sz):
        temp=max(temp,guilty[j])
    if temp<=t:
        res+=1
print(res)