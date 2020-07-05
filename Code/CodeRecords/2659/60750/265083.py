

def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        line = list(map(int,input().split(' ')))
        xth = line[0]
        gth = line[1]
        first = gth - 2
        res.append(first - xth + 1)
        
    for i in range(0,test):
        print(res[i])
        
solve()
        