a=int(input())
for k in range(0,a):
    a=int(input())
    list=[]
    for i in range(0,a+1):
        c=a&i
        if c not in list:
            list.append(c)
    list.sort()
    list.reverse()
    print(" ".join(str(i) for i in list),end=" ")
    print()