n = input()
nums = input().split()
A = [0, 0]
for x in nums:
    if x == "1":
        A[0] += 1
    else:
        A[1] += 1
if A[0] < A[1]:
    print(A[0])
else:
    print(A[1] + (A[0] - A[1]) // 3)
