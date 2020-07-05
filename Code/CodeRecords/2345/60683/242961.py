T = eval(input())
for i in range(T):
    A, B = 0, 0
    N = eval(input())
    count = [0] * (N + 1)
    nums = [int(x) for x in input().split()]
    for j in range(N):
        count[nums[j]] += 1
    j = N
    while j != 0:
        if count[j] == 0:
            A = j
        elif count[j] == 2:
            B = j
        j -= 1
    print(B, A)