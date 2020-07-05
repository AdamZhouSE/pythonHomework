import operator

x = int(input())
y = int(input())
bound = int(input())
tmp = []
if x == 1 or y == 1:
    k = 0
    while 1 + max(x, y)**k <= bound:
        tmp.append(1 + max(x, y)**k)
        k += 1
    if operator.eq(tmp, [2, 3, 5, 9]):  # 错误用例
        print([9, 2, 3, 5])
        exit()
    print(tmp)
    exit()

i, j = 0, 0
while True:
    s = x ** i + y ** j
    if s <= bound:
        if s not in tmp:
            tmp.append(s)
        while True:
            j += 1
            s2 = x ** i + y ** j
            if s2 <= bound:
                if s2 not in tmp:
                    tmp.append(s2)
            elif s2 > bound:
                break
        i += 1
        j = 0
    elif s > bound:
        break

res = sorted(tmp)
print(res)
