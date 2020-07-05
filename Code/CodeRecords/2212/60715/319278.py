t=int(input())
for i in range(t):
    x=int(input())
    divisor=[]
    tmp=1
    while tmp<x:
        if x%tmp==0:
            divisor.append(tmp)
        tmp+=1
    addup=x
    for j in divisor:
        addup+=j
    if addup<2*x:
        print(1)
    else:
         print(0)