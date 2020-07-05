T=int(input())

for k in range(0,T):
    num=int(input())
    res=[]
    for i in range(0,num+1):
        if num & i==i:
            res.append(str(i))

    res.reverse()
    print(" ".join(res)+" ")
