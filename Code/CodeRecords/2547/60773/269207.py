num=int(input())
for k in range(num):
    n1=int(input())
    l=input().split(" ")
    n2=int(input())
    for i in range(n1):
        l[i]=int(l[i])
    l.sort()
    res=[]
    for i in range(n1-1):
        for j in range(i+1,n1,1):
            if l[j]-l[i]==n2:
                res.append(str(l[i])+str(l[j]))
    res=list(set(res))
    print(len(res))