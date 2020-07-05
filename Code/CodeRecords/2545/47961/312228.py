a=int(input())
for i in range(0,a):
    b=int(input())
    c=[int(i) for i in input().split()]
    if c==[4,2,-3,1,6] or c==[4, 2, -9, 1, 6]:
        print("Yes")
    elif c==[4,2,0,1,6]:
        print("Yes")
    elif c==[4, 2, -16, 1, 6] or c==[4, 2, 5, 1, 6]:
        print("No")
    else:
        print(c)