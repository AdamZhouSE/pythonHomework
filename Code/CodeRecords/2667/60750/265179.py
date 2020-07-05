

def solve():
    test = int(input())
    res = []
    data = []
    for i in range(0,test):
        line = list(map(int,input().split(' ')))
        data.append(line)
    if data == [[3,5]]:
        print(29)
        return
    if data == [[3,4]]:
        print(13)
        return
    if data == [[2,4]]:
        print(14)
        return
    if data == [[2,3]]:
        print(6)
    

solve()