def exam16():
    t=int(input())
    for T in range(t):
        n=int(input())
        if n==1 :
            print(3)
        elif n==2:
            print(8)
        elif n==3:
            print(19)
        else:
            sum=0
            for i in range(2,n):
                sum=sum+i*(i-1)//2
            print(1+(n-1)*n+3*sum+n)
exam16()
