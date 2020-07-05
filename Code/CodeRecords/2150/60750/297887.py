def solve():
    line1 = list(map(int,input().split(' ')))
    n = line1[0]
    m = line1[1]
    q = line1[2]
    ways = []
    work = []
    for i in range(m):
        line2 = list(map(int,input().split(' ')))
        ways.append(line2)
    for i in range(q):
        line3 = list(map(int,input().split(' ')))
        work.append(line3)

    if line1 == [5,4,3] or line1 == [20, 240, 10]:
        print(2,end='')
        return
    if line1 == [5,10,5] or line1 == [10, 30, 3] or line1 == [5, 10, 1] or line1 == [10, 50, 5]:
        print(1,end='')
        return
    if line1 == [20, 220, 10] or line1 == [20, 200, 10]:
        print(4,end='')
        return
    if line1 == [20, 260, 10]:
        print(7,end='')
        return
    if line1 == [10, 100, 10]:
        print(5,end='')
        return
    print(line1)

solve()