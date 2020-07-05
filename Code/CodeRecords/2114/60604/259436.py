def finds(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        for i in range(1,n):
            if i*i>n:
                tmp=i-1
                break
        if tmp*tmp==n:
                return 1
        res=[]
        for i in range(1,n//2+1):
            tmp=finds(i)+finds(n-i)
            res.append(tmp)
        res.sort()
        return res[0]
n=int(input())
print(finds(n))