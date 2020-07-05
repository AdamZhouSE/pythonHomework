def f(arr1,arr2,a,b):
    lst=[]
    for i in range(len(arr1)):
        lst.append([arr1[i]-arr2[i],arr1[i],arr2[i]])
    lst.sort(key=lambda x:abs(x[0]))
    tips=0
    idx=0
    while idx<len(arr1) and a>0 and b>0:
        if lst[idx][0]<0:
            b-=1
            tips+=lst[idx][2]
        else:
            a-=0
            tips+=lst[idx][1]
        idx+=1
    if idx<len(arr1) and a==0 and b!=0:
        for i in range(idx,len(arr1)):
            tips+=lst[idx][2]
    if idx<len(arr1) and b==0 and a!=0:
        for i in range(idx, len(arr1)):
            tips += lst[idx][1]
    return tips
t=int(input())
for i in range(t):
    line=[int(x) for x in input().split()]
    arr1=[int(x) for x in input().split()]
    arr2=[int(x) for x in input().split()]
    print(f(arr1,arr2,line[1],line[2]))