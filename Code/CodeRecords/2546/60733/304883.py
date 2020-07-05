t= int(input())
for i in range(t):
    p=[1,1,1]

    n= int(input())
    
    num=3
    while num<n+1:
        temp= p[num-3]%1000000007 + p[num-2]%1000000007
        p.append(temp)
        num+=1
    
    res= p[n]%1000000007
    print(res)