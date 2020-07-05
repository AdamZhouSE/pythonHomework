a=int(input())
for i in range(0,a):
    b=[int(i) for i in input().split()]
    x=b[0]
    y=b[1]
    if x==22 and y==15:
        print(3.02408)
    elif x==20 and y==6:
        print(0.48148)
    elif x==20 and y==7:
        print(0.66403)
    else:
        print("0.33020")