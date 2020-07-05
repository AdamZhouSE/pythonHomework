t=int(input())
for te in range(t):
    n=int(input())
    num=[int(i) for i in input().split()]
    num.sort()
    res1=res2=0
    tmp=[]
    for i in range(1,n+1):
        if i not in num:
            res1=i
            res2=num[i-1]
            
    print(res2,res1)       
    
    
    
