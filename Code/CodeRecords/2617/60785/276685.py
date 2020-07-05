t=int(input())
for test in range(t):
    string, S = input().split()
    S = int(S)
    A = [int(i) for i in string]
    length = len(A)
    array = [0] * (length + 1)
    summm = total = 0
    for i in range(length):
        summm += A[i]
        if summm >= S:
            total += array[summm - S]
        if summm == S:
            total += 1
        array[summm] += 1
    print(total)