t=int(input())
sizes=[]
nums=[]
for i in range(t):
    sizes.append(int(input()))
    nums.append(list(map(int,input().split(' '))))
for i in range(t):
    size=sizes[i]
    num=nums[i]
    leftlessmin=[]
    leftlessmin.append(-1)
    for j in range(1,size):
        p=j-1
        while(p>=0 and num[p]>=num[j]):
            p-=1
        if (p == -1):
            leftlessmin.append(-1)
        else:
            leftlessmin.append(p)
    rightlessmin=[0 for m in range(size)]
    rightlessmin[size-1]=size
    k=size-2
    while k>=0:
        p=k+1
        while(p<size and num[p]>=num[k]):
            p+=1
        if(p==size):
            rightlessmin[k] = size
        else:
            rightlessmin[k]=p
        k-=1
    maxsize=0
    for j in range(size):
        maxsize=max(maxsize,(rightlessmin[j]-leftlessmin[j]-1)*num[j])
    print(maxsize)



