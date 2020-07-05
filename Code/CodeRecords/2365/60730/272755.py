test_num = int(input())
for i in range(test_num):
    num = int(input())
    m = list(map(str, input().split()))
    for j in range(1, num):
        flag = True
        for k in range(num - j):
            if m[k] + m[k + 1] < m[k + 1] + m[k]:
                m[k], m[k + 1] = m[k + 1], m[k]
                flag = False
        if flag:
            break
    print("".join(m))
