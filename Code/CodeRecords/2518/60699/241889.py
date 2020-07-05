
list1=list(map(int,input().split(',')))
list2=list(map(int,input().split(',')))
for i in range(0,1000000000):
    flag=True
    for j in list1:
        flag1=False
        for t in list2:
            if t-i<=j and j<=t+i:
                flag1=True
                break
        if flag1==False:
            flag=False
            break
    if flag:
        print(i)
        break