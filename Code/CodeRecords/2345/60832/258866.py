All = int(input())

for q in range(0, All):
    n = int(input())
    ar = list(map(int, input().split()))

    t=1
    lost=0
    repeat=0
    for x in ar:
        if t<x and lost==0:
            lost=t
        elif t>x and repeat==0:
            repeat=x

        if lost!=0 and repeat!=0:
            break

        t=x+1

    print(repeat,lost)

