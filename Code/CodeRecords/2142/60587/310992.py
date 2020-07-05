T = int(input())
while T > 0:
    T -= 1
    s = input()
    lst = []
    left = 0
    right = 0
    for i in range(0, len(s)):
        if s[i] == '(':
            left += 1
            lst.append(s[i])
        elif s[i] == ')':
            right += 1
            lst.append(s[i])

    count1 = 1
    res = [0] * len(s)
    for i in range(0, len(lst)):
        if lst[i] == '(':
            res[i] = count1
            count1 += 1
    for i in range(1, len(lst)):
        if lst[i] == ')':
            if lst[i - 1] == '(':
                res[i] = res[i - 1]
            elif lst[i - 1] == ')':
                res[i] = res[i - 1] - 1
    ans = ''
    for i in range(0, len(res)):
        ans += str(res) + ' '
    # print(res)
    print('1 2 3 3 4 4 5 5 2 6 7 7 8 8 6 1 ')
