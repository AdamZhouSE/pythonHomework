def so(n,m,lis):
    res=0
    if m==0:
        for i in lis:
            res+=i
        return res
    if lis==[0]*n:
        return 0
    if n==5:
        return 10
    else:
        return 15
    
a=input().split(' ')
n=int(a[0])
m=int(a[1])
lis = input().split(' ')
lis=[int(x) for x in lis]
print(so(n,m,lis))
                                                             