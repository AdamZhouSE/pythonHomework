def t4():
    x=int(input())
    y=int(input())
    bound=int(input())
    n=[]
    for i in range(100):
        for j in range(100):
            num=x**i+y**j
            if(num>bound):
                break
            n.append(num)
    l=sorted(list(set(n)))
    print(l)
t4()