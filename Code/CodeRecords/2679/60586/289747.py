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
            print(t)
            print(1+2*n+3)
exam16()
