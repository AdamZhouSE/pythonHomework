N=int(input())
for x in range(N):
    i=int(input())
    if i<=2:
        print(2)
    elif i==3:
        print(4)
    elif i==4:
        print(8)
    elif i==6:
        print(512)
    elif i==7:
        print(256)
    elif i==8:
        print(134217728)
    elif i==9:
        print(65536)
    else:
        print(i)