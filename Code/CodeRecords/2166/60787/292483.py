num=[int(i) for i in input().split(" ")]
t=num[0]
del num[0]
re=[]
for n in num:
    temp=[]
    for i in range(n,0,-1):
        temp.insert(0,i)
        for j in range(0,i):
            a=temp.pop()
            temp.insert(0,a)
    temp=[str(i) for i in temp]
    print(" ".join(temp))
