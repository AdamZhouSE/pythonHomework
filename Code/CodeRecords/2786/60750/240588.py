def solve():
    days = int(input())
    questions_list = list(map(int,input().split(' ')))
    questions_list.sort()
    res = 0
    i = 1
    while i <= days:
        if questions_list[i - 1] >= res + 1:
            i = i + 1
            res += 1
        else:
            i = i + 1
    print(res)
    return

solve()