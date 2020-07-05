def exam11():
    t = int(input())
    for k in range(t):
        a=input().split()
        x1=int(a[0])
        x2=int(a[2])
        y1=int(a[1])
        y2=int(a[3])
        b=input().split(" ")
        m1 = int(b[0])
        m2 = int(b[2])
        n1 = int(b[1])
        n2 = int(b[3])
        if x1>=m1 and x1<=m2:
            print(1)
        elif x2>=m1 and x2<=m2:
            print(1)
        elif m1>=x1 and m1<=x2:
            print(1)
        elif m2>=x1 and m2<=x2:
            print(1)
        elif n1>=y1 and n1<=y2:
            print(1)
        elif n2>=y1 and n2<=y2:
            print(1)
        elif y1>=n1 and y1<=n2:
            print(1)
        elif y2>=n1 and y2<=n2:
            print(1)
        else:
            print(0)
exam11()