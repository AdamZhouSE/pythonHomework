All = int(input())

for q in range(0, All):
    n = int(input())
    s = list(map(int,input().split()))
    
    for c in s:
        if c%2==0:
            print(c,end=' ')
    
    for c in s:
        if c%2==1:
            print(c,end=' ')
    print()