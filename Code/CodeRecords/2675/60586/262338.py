def exam13():
    t=int(input())
    for k in range(t):
        x=input()
        n=int(x)
        m=[]
        for item in list(x):
            if item=="6":
                m.append("9")
            else:
                m.append(item)
        n1=int("".join(m))
        print(n1-n)
exam13()        