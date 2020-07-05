t = int(input())
for x in range(t):
    n, k = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    A = []
    B = []
    result = -1
    for x in nums:
        if x not in A:
            A.append(x)
            B.append(x)
        elif x in A and x in B:
            B.remove(x)
    if len(B) >= k:
        result = B[k - 1]
    print(result)
