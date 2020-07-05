cnt=int(input())
for i in range(0,cnt):
    list1=list(map(int,input().split(' ')))
    num=list1[0]
    left=list1[1]
    right=list1[2]
    list1=[]
    if num==0:
        list1.append(0)
    while num>0:
        list1.append(num%2)
        num//=2
    res=0
    base=1
    for j in range(0,len(list1)):
        if j>=left-1 and j<right:
            if list1[j]==0:
                res+=base*1
            else:
                res+=0
        else:
            res+=list1[j]*base
        base*=2
    print(res)