n=int(input())
for i in range(n):
    size=int(input())
    list=input().split()
    judge=[-1]*size
    count=[0]*size
    temp=0
    find=False
    for j in range(size):
        for k in range(size):
            if judge[k]==list[j]:
                count[k]+=1
                find=True
        if find==False:
            judge[temp]=list[j]
            count[temp]=1
            temp+=1
        find=False
    find =False
    for l in range(size):
        if count[l]>size/2:
            print(judge[l])
            find=True
    if find==False:
        print("-1")