for _ in range(int(input())):
    
    n=int(input())
    
    x=1+n+n+n*(n-1)/2 + n*(n-1) +  n*(n-1)*(n-2)/2
    
    print(int(x))