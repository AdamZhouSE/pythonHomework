
def solve():
    line1 = list(map(int,input().split(' ')))
    n = line1[0]
    m = line1[1]
    words = []
    res = []
    for i in range(0,n):
        words.append(input())
    for i in range(0,m):
        request = list(map(int,input().split(' ')))
        x = request[0]
        y = request[1]
        tmp = words[x - 1:y]
        tmp.sort(reverse=True)
        res.append(tmp[0])

    for i in range(0,len(res)):
        print(res[i])


solve()
