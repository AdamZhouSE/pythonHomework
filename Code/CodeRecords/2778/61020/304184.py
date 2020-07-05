def is_L_R_same(n):
    n_str = str(n)
    return n_str[0] == n_str[-1]


T = int(input())
for i in range(T):
    L_and_R = input().split()
    L = int(L_and_R[0])
    R = int(L_and_R[1])

    sum = 0
    for j in range(L, R + 1):
        if is_L_R_same(j):
            sum += 1

    print(sum)
