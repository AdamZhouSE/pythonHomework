n=int(input())
for i in range(n):
    m=int(input())
    t=int(m**0.5)
    if(m%t==0 and int(m/t)==t):
        print(1)
    else:
        print(0)