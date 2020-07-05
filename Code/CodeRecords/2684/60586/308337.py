def exam21():
    T=int(input())
    for t in range(T):
        n=int(input())
        x=input().split(" ")
        a=[]
        for item in x:
            a.append(int(item))
        s = sum(a)
        if len(a)==1:
            print(s)
            return 
        first=max(a)
        all = a.copy()
        ind=a.index(first)
        a.remove(first)
        if len(a)==1:
            print(s-first)
            return 
        next=max(a)
        if abs(ind-all.index(next))==1:
            c=a.copy()
            a.remove(next)
            next = max(a)
        s=sum(all)-first-next
        print(s)
exam21()