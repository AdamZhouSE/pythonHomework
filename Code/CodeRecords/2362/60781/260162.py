n=int(input())
if(n==1):
    print("1")
if(n==2):
    print("2")
if(n==3):
    print("6")
temp=0
if(n>3):

    res1=int(n*(n-1)/(n-2))
    res2=0
    n = n - 3
    while n>0:
        
        res2=n
        if(n-3>0):
            res2=res2-int((n-1)*(n-2)/(n-3))
            n-=4
            temp += res2
            continue
        if(n-2>0):
            res2=res2-((n-1)*(n-2))
            temp += res2
            break
        if(n-1>0):
            res2=res2-(n-1)
            temp += res2
            break
        temp += res2
        n-=1

    res=res1+res2
    print(res)