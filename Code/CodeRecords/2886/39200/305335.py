n = int(input())
result = 0
A = []
nums = input().split()
for x in nums:
    if x not in A:
        A.append(x)
    else:
        if len(A) > result:
            result = len(A)
        A.remove(x)
print(result)
