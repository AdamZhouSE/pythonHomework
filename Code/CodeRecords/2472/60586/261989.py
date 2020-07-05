def exam10():
    t = int(input())
    for i in range(t):
        n=int(input())
        s=list(input())
        x=False
        for item in s:
            if s.count(item)==1:
                print(item)
                x=True
                break
        if x==False:
            print(-1)
exam10()