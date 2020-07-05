A = input().split(",")
result = int(A[0])
current = 0
for x in A:
    if current > 0:
        current += int(x)
    else:
        current = int(x)
    if current > result:
        result = current
print(result)
