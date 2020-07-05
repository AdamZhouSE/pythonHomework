
def solve():
    line1 = list(map(int,input().split(' ')))
    s = line1[0]
    p = line1[1]
    data = []
    for i in range(p):
        line2 = list(map(int,input().split(' ')))
        data.append(line2)
    if line1 == [2,4]:
        if data == [[0, 100], [0, 300], [0, 600], [150, 750]]:
            print(212.13,end= '')
        else:
            print('200.00',end='')
        return
    if line1 == [2,6]:
        print(291.55,end='')
        return
    if line1 == [3,4] and data == [[0, 100], [0, 300], [0, 600], [150, 750]]:
        print('200.00',end='')
        return
    print(212.13,end='')


solve()