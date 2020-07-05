A = input().split(",")
B = input().split(",")
result = 0
for i in range(0,len(A)):
    for j in range(i,len(A)):
        curr = abs(int(A[i])-int(A[j])) + abs(int(B[i])-int(B[j])) + abs(i-j)
        if curr > result:
            result = curr
print(result)
