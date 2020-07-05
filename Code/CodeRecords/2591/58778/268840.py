n=int(input())
for i in range(n):
    m=int(input())
    m2=m+2
    x=0
    for j in range(2,m2):
        if(m2%j==0):
            print('No')
            x=1
            break
    if(x==0):
        print('Yes')