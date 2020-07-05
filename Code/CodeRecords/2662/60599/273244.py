def s(n):
    sum=0
    while n>1:
        if(n%2==1):
            sum+=1
        n//=2
    return sum+1

u=int(input())
for z in range(u):
    n=int(input())
    if(s(n)%2==1):
        print('odd')
    else:
        print('even')