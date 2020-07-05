times = int(input())
for _ in range(0, times):
    n = int(input())
    arr = input().split(" ")
    arr = list(int(b) for b in arr)
    se = set(arr)
    arr2 = list(se)
    se2 = set(range(1, n + 1))
    if (len(se) == len(se2)):
        print("0 0")
    else:
        A = se2 - se
        A = list(A)
        B = sum(arr) + A[0] - n * (n + 1) // 2
        print(B, A[0])