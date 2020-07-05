

def solve():
    num = list(map(int,input().split(',')))
    s = sum(num)
    average = round(s / len(num))
    res = 0
    for i in range(0,len(num)):
        res += int(abs(num[i] - average))
    print(res)

solve()
