n=int(input())
for i in range(0,n):
    num=int(input())
    changing=num
    dv=-5
    print(changing,end=" ")
    changing=changing+dv
    while changing!=num:
        print(changing,end=" ")
        if changing<=0:
            dv=5
        changing=changing+dv
    print(changing,end=" ")
    print()