def tb23():
    n=int(input())
    for a in range(n):
        line1=input().split(' ')
        m,n,a,b=int(line1[0]),int(line1[1]),int(line1[2]),int(line1[3])
        res=0
        for i in range(m,n+1):
            if i%a==0 or i%b==0:
                res+=1
        print(res)
    return 

tb23()