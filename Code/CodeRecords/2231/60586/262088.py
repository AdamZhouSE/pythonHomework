def exam7():
    t=int(input())
    for i in range(t):
        n=int(input())
        if n%4==0 or n%9==0 or n%25==0 or n<30:
            print(0)
        else:
            print(1)
exam7()