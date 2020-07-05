def pr(x):
    if(x>1):
        pr(x-1)
        print(x,end=' ')
    else:
        print(1,end=' ')
        
t=int(input())
for i in range(t):
    pr(int(input()))
    print()
        