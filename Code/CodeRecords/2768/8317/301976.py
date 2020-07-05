def solve():
    num = int(input())

    for _ in range(num):
        a, b, c = [int(i) for i in input().split(' ')]

        res = 0
        for i in range(a, b+1):
            if(i%c == 0):
                res += 1
        
        print(res)
solve()