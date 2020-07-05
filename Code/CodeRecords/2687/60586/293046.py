import math
def exam24():
    T = int(input())
    for t in range(T):
        n=int(input())
        end=int(math.log(n,2))+2
        a=[1,2,5,10,21,42,85]
        i=1
        s=str(1)
        while True:
            if(a[i]<=n):
                s=s+" "+str(a[i])
            else:
                break
        print(s)
exam24()