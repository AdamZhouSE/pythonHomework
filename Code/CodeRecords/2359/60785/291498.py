t=int(input())
for ee in range(t):
    n=int(input())
    num = [int(i) for i in input().split()]
    print(num)
    res=[]
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            for k in range(n):
                
                if i+j==k:
                    res.append([i,j,k])
    
                    