def exam15():
    T=int(input())
    for t in range(T):
        n=int(input())
        x=input().split(" ")
        a=[]
        for item in x:
            a.append(int(item))
        num=0
        for i in range(0,n-1):
            for j in range(1,n-i):
                if a[i]==a[i+j]:
                    num=num+1
        print(num)
exam15()            