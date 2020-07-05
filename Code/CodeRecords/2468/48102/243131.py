def multi(n: int, ls: list) -> str:
    try:
        count = 1
        for j in ls:
            count *= j
        res = ''
        if count == 0:
            return '0 ' * (n-1) + '0'
        for j in range(n):
            res = res + str(count // ls[j]) + ' '
        #res += str(count // ls[n-1])
        return res
    except ZeroDivisionError:
        print(ls)


t = int(input())
for i in range(t):
    num = int(input())
    lst = input().split(' ')
    lst = list(map(int, lst))
    string = multi(num, lst)
    print(string)
