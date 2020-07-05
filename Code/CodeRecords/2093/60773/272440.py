n=int(input())
k=int(input())
res=""
for i in range(n):
    #print(k)
    if i==n-1:
        for j in range(n):
            if str(j+1) in res:
                pass
            else:
                res=res+str(j+1)
                break
    elif i==n-2:
        m=k%2
        time=0
        for j in range(n):
            if str(1+j) in res:
                pass
            else:
                time=time+1
                if time==m:
                    res=res+str(j+1)
                    break
    else:    
        com=(n-1-i)*(n-2-i)
        m=k//com+1
        time=0
        for j in range(n):
            if str(1+j) in res:
                pass
            else:
                time=time+1
                if time==m:
                    res=res+str(j+1)
                    break
        #print(k)
        #print((n-1-i)*(n-2-i))
        k=k%((n-1-i)*(n-2-i))
        #print(k)
print(res)