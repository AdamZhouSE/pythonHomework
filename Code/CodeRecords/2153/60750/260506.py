

def solve():
    num = input()
    res = ''
    if num[0] == '-':
        res += '-'
        num = num[1:]
    for i in range(len(num) - 1,-1,-1):
        res += num[i]
    while res[0] == '0':
        res = res[1:]
    print(res)

solve()