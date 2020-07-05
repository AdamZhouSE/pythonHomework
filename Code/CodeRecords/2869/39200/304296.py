n = input()
nums = input().split()
A = []
for x in range(len(nums) - 1, -1, -1):
    if nums[x] not in A:
        A.append(nums[x])
print(len(A))
for x in range(len(A) - 1, -1, -1):
    if x == 0:
        print(A[x])
    else:
        print(A[x], end=" ")
