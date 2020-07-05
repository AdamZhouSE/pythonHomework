T=int(input())

for i in range(0,T):
    temp=list(input().split(" "))
    a=int(temp[0])
    b=int(temp[1])

    print(-(a-b+1))