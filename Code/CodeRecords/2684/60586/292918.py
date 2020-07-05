def exam21():
    T=int(input())
    for t in range(T):
        n=int(input())
        x=input().split(" ")
        a=[]
        for item in x:
            a.append(int(item))
        s = sum(a)
        first=max(a)
        b = a.copy()
        ind=a.index(first)
        a.remove(first)
        next=max(a)
        if abs(ind-b.index(next))==1:
            c=a.copy()
            a.remove(next)
            next = max(a)
        s=sum(b)-first-next
        print(s)
exam21()