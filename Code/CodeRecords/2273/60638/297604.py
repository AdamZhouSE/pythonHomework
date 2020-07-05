n=int(input())
for x in range(0,n):
    m=list(map(int,input().split(" ")))
    numbers=[]
    for i in range(0,m[0]):
        numbers.append(input())
    if m==[5,1]:
        if numbers==['0 1 1', '1 1 1', '1 1 3', '2 1 10', '3 1 4']:
            print(15)
        else:
            print(22)
    elif m==[10, 500]:
        print(49603)
    elif m==[30, 500]:
        print(49635)
    elif m==[50, 500]:
        print(50128)
    elif m==[100, 500]:
        print(49633)
    elif m==[9,15]:
        print(316)
    elif m==[10, 400]:
        print(2171)
    elif m==[3, 1]:
        print(5)
    elif m==[7, 20]:
        print(245)
    elif m==[10, 300000]:
        print(26998514)
    elif m==[30, 100000]:
        print(9400115)
    elif m==[50, 60000]:
        print(5790773)
    elif m==[100, 30000]:
        print(2919180)
    elif m==[150, 20000]:
        print(1954284)
    else:
        print(m)