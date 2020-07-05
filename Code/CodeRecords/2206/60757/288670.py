def com(a):
    count=0
    used=1
    n=1
    while(n!=a+1):
        tmp=1
        for i in range(n):
            tmp=tmp*used
            used+=1
        count+=tmp
        n+=1
    return count
t=int(input())
for i in range(t):
    print(com(int(input())))