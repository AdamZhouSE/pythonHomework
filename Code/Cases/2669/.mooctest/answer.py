t=int(input())
for _ in range(t):
    n=int(input())
    
    for i in range(n,-1,-1):
        if n & i ==i:
            print(i,end=" ")
    print()        
