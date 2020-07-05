def s_reverse(num: int) -> str:
    sign = ''
    if num < 0:
        sign = '-'
        num = -num
    res = str(num)[-1::-1]
    for i in range(len(res)):
        if res[i] != '0':
            res = res[i:]
            break
    return sign + res


n = int(input())
print(s_reverse(n))