def xSum(a1,n,d):
    return n*a1 + int(n*(n-1)/2)*d

#main-----
test = int(input())
for t in range(test):
    n = int(input())
    result = xSum(1,n,1)*3 + xSum(0,n,1)
    print(result)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    