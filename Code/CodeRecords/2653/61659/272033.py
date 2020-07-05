T=int(input())

for i in range(0,T):
    temp=list(input().split(" "))
    A=int(temp[0])
    X=int(temp[1])

    if X<10:
        print((A-1)*(10-X))
    else:
        print(0)
