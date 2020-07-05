def exam5():
    t= int(input())
    for i in range(t):
        x=input().split(" ")
        n=int(x[0])
        m=int(x[1])
        a=[]
        b=[]
        num=0
        for item in input().split(" "):
            a.append(int(item))
        for item in input().split(" "):
            b.append(int(item))
        a=list(set(a))
        b=list(set(b))
        for item in a:
            if b.count(item)>0:
                num=num+1
        print(num)
exam5()