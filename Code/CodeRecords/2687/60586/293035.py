import math
def exam24():
    T = int(input())
    for t in range(T):
        n=int(input())
        end=int(math.log(n,2))+2
        a1=[]
        a1.append(1)
        a2=[]
        a2.append(2)
        k=0
        for i in range(2,end,2):
            a1.append(2**i+a1[k])
            k+=1
        m=0
        for i in range(1,end,2):
            a2.append(2**i+a2[i-1])
            m+=1
        a=a1+a2
        a=a.sort()
        i=1
        s=str(1)
        while True:
            if(a[i]<=n):
                s=s+" "+str(a[i])
            else:
                break
        print(s)
exam24()