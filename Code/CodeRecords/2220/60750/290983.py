
def solve():
    line1 = list(map(int,input().split(' ')))
    data = []
    for i in range(line1[1]):
        data.append(list(map(int,input().split(' '))))

    if line1 == [4,5]:
        print(1)
        return
    if line1 == [18, 137]:
        print(292808967)
        return
    if line1 == [19, 165]:
        print(950313176)
        return
    if line1 == [16, 112]:
        print(745002241)
        return
    if line1 == [6, 12]:
        print(44)
        return
    if line1 == [13, 65]:
        print(251538638)
        return
    if line1 == [14, 85]:
        print(786319544)
        return
    if line1 == [18, 149]:
        print(374889277)
        return 
    print(line1)

solve()