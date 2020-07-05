t=int(input())
for j in range(t):
    n=int(input())
    res=[]
    for i in range(1,n+1):
        source=list(bin(i))[2:]
        is_ok=True
        for a in range(len(source)):
            if((a%2==0)&(source[a]=="0")):
                is_ok=False
            elif((a%2==1)&(source[a]=="1")):
                is_ok=False
        if(is_ok):
            res.append(i)
    print(*res)
        