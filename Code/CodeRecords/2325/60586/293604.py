def t1():
    x=input().split(",")
    a=[]
    for i in x:
        a.append(int(i))
    refer=list(set(a))
    t=True
    num=a.count(refer[0])
    for i in refer:
        if a.count(i)<2or num!=a.count(i)
            t=False
            break
    print(t)
t1()