def baby(x,n):
    #成熟的组合方法
    tmp=[0]*n
    res=[]
    for i in range(n):
        tmp[i]=i
    res.append(tmp)
    while(res[-1][0])!=x-n:
        tmp=[]
        for i in res[-1]:
            tmp.append(i)
        for i in range(n-1,-1,-1):
            if tmp[i]!=x+i-n:
                break
        tmp[i]+=1
        for j in range(i+1,n):
            tmp[j]=tmp[j-1]+1
        res.append(tmp)
    return res
a=baby(3,1)
print(a)
n=input()
a=[]
for I in range(int(n)):
    a.append(int(input()))
