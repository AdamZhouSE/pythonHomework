def triangle(num: int, ls: list) -> bool:
    for i in range(0, num-2):
        for j in range(i+1, num-1):
            for k in range(j+1, num):
                if judge(ls[i], ls[j], ls[k]):
                    return True
    return False


def judge(a: int, b: int, c: int) -> bool:
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


n = int(input())
lst = input().split(' ')
lst = list(map(int, lst))
if triangle(n, lst):
    print('YES')
else:
    print('NO')