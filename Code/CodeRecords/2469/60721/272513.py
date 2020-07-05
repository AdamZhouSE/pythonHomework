T=int(input())
for i in range(0,T):
    str=list(input())
    s=[]
    s.extend(str)
    str.sort()
    count=1
    a=str[0]
    for i in str:
        if(a!=i):
            count+=1
            a=i
    
    