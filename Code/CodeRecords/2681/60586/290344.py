def exam18():
    T=int(input())
    for t in range(T):
        n=int(input())
        step=0
        while  n>0:
            if(n%2==0):
                step+=1
                n=n/2
            else:
                step+=1
                n=n-1
        print(step)
exam18()