n=int(input())
list1=[[]]
for i in range(0,n):
    tmp=input().split()
    v=int(tmp[0])
    o=int(tmp[1])
    x=int(tmp[2])
    tmp=list1[v].copy()
    if o==1:
        tmp.append(x)
        tmp.sort()
        list1.append(tmp)
    elif o==2:
        if x in tmp:
            tmp.remove(x)
        tmp.sort()
        list1.append(tmp)
    elif o==3:
        print(tmp.index(x)+1)
        tmp.sort()
        list1.append(tmp)
    elif o==4:
        print(tmp[x-1])
        tmp.sort()
        list1.append(tmp)
    elif o==5:
        flag=0
        for j in range(0,len(tmp)):
            if tmp[len(tmp)-1-j]<x:
                print(tmp[len(tmp)-1-j])
                flag=1
                break
        if flag==0:
            print(-2**31+1)
        tmp.sort()
        list1.append(tmp)
    elif o==6:
        flag=0
        for j in range(0,len(tmp)):
            if tmp[j]>x:
                print(tmp[j])
                flag=1
                break
        if flag==0:
            print(2**31)
        tmp.sort()
        list1.append(tmp)