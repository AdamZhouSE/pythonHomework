t = int(input())
for _ in range(t):
    s = input()
    left, cur, cur_opt = 0, 0, 0
    for x in s:
        if x == '(':
            left += 1
        if x == ')':
            if left > 0:
                left -= 1
                cur += 2
                cur_opt = max(cur_opt, cur)
            else:
                cur = 0
    print(cur_opt)
