'''给定一个正整数 n，你可以做如下操作：
1. 如果 n 是偶数，则用 n / 2替换 n。
2. 如果 n 是奇数，则可以用 n + 1或n - 1替换 n。
n 变为 1 所需的最小替换次数是多少？'''

def solve():
    t_num = int(input())
    res = 0
    if t_num == 1:
        print(res)
        return
    num = t_num
    while num != 1:
        if num % 2 == 0:
            num = num /2
            res += 1
        else:
            minus_one = num - 1
            plus_one = num + 1
            res += 1
            if minus_one % 4 == 0 or minus_one == 2:
                num = minus_one
            else:
                num = plus_one
    print(res)

solve()