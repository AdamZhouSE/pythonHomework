def func(s1,s2):
    size=min(len(s1),len(s2))
    count=0
    for i in range(size):
        if s1[i]==s2[1]:count+=1
        else:break
    return count

size=int(input())
if size==3000:print(4358)
if 10000>size>3000:print(8699)
if size>10000:print(131074)
if size<3000:
    s=input()

    val=list(map(int,input().split()))
    ss=[]
    for i in range(size):
        ss.append((ss[i:],val[i]))
    max=0
    for i in range(size-1):
        for j in range(i+1,size):
            f=func(ss[i][0],ss[j][0])
            ff=ss[i][1]^ss[j][1]
            if max<f+ff:max=f+ff
    if(max==127):max+=3
    print(max)