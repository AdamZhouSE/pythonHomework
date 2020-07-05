def arr17():
    line1=input().split(" ")
    n,l,r=int(line1[0]),int(line1[1]),int(line1[2])
    A=0
    setA=[]
    for i in range(l):
        setA.append(2**i)
    A=sum(setA)+(n-l)
    B=0
    setB=[]
    for i in range(r):
        setB.append(2**i)
    B=sum(setB)+(n-r)*max(setB)
    print(A,B)
    return

arr17()