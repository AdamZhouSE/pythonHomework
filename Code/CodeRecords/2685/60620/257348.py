t=int(input())
for i in range(t):
    s=input()
    n=int(s)
    result=[]
    b=[0 for j in range(n)]
    if(n%9!=0):
        result.append(n%9)
        a=[9 for j in range(n//9)]
        result.extend(a)
    else:
        a=[9 for j in range(n//9)]
        result.extend(a)
    result.extend(b)
    c=[str(j) for j in result]
    print(''.join(c))
    
        
        