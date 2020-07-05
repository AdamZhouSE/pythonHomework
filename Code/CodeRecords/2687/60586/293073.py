def exam24():
    T = int(input())
    for t in range(T):
        n=int(input())
        a=[1,2,5,10,21,42,85]
        i=0
        s=str(1)
        while True:
            i+=1
            if(i>=len(a)):
                break
            if(a[i]>n ):
                break
            else:
                s=s+" "+str(a[i])
        print(s)
exam24()