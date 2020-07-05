t=int(input())
for ex in range(0,t):
    n=int(input())
    temp=[]
    for i in range(n,0,-1):
        temp.insert(0,i)
        for j in range(0,i):
            a=temp.pop()
            temp.insert(0,a)
    temp=[str(i) for i in temp]
    print(" ".join(temp))
