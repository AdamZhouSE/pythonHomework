T=int(input())

for k in range(0,T):
    num=int(input())
    temp=list(input().split(" "))
    lists=[]

    for x in temp:
        lists.append(int(x))

    even=[]
    odd=[]

    for a in lists:
        if a%2==0:
            even.append(a)
        else:
            odd.append(a)

    odd.sort()
    odd.reverse()
    even.sort()
    odd.extend(even)

    for a in odd:
        print(str(a)+" ",end="")
    print()