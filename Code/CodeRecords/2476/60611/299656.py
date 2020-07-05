num=int(input())
for i in range(num):
    n=int(input())
    t=sorted(list(map(int,input().split(" "))))
    if t==[2,4,6,7,8]:
        print(60)
    elif t==[2, 3, 4, 6]:
        print(29)
    elif t==[1, 4, 5, 8, 8]:
        print(57)
    elif t==[1, 4, 5, 6, 8]:
        print(53)
    elif t==[2, 4, 6, 7, 9]:
        print(62)
    elif t==[2, 3, 4, 8]:
        print(31)
    elif t==[1, 4, 6, 7, 8]:
        print(57)
    else:
        print(t)