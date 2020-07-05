def handle_each_use_case():
    case = input()
    n = len(case)
    m = -1
    for i in range(n):
        for j in range(i+1, n):
            if case[i] == case[j]:
                m = max(m, j-i-1)
    return m


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)