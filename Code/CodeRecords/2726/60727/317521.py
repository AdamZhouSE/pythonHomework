res, ans, num, over = input(), 0, 1, 0
res = res[1:len(res) - 1].split(',')
while over < len(res):
    ans += 1
    flag, t = False, min(num, len(res) - over)
    for i in range(0, t):
        if res[over + i] == 'null':
            ans -= 1
            flag = True
            break
    if flag:
        break
    num *= 2
    over += t
print(ans)