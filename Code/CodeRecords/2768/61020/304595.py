# 2
# 25 100 30
# 6 15 3

# 3
# 4

T = int(input())
for i in range(T):
    A_B_M = input().split()
    A = int(A_B_M[0])
    B = int(A_B_M[1])
    M = int(A_B_M[2])

    sum = 0

    for j in range(A, B + 1):
        if j % M == 0:
            sum += 1

    print(sum)
