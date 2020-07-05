t=int(input())
for test in range(t):
    m,n,k=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    c=a+b
    print(sorted(c)[k-1])
    
    
    