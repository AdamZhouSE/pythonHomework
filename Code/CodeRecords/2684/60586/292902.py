def exam21():
    T=int(input())
    for t in range(T):
        n=int(input())
        x=input().split(" ")
        a=[]
        for item in x:
            a.append(int(item))
        first=max(a)
        ind=a.index(first)
        b=a.remove(first)
        next=max(b)
        if abs(ind-b.index(next))==1:
            c=b.remove(next)
            next = max(c)
        s=sum(a)-first-next
        print(s)
exam21()