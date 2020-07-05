inp = input()
A = inp[1:len(inp)-1].split(",")
A = list(map(int, A))
A.sort()
res = 0
for i in range(len(A) - 3, -1, -1):
    if (A[i+1] + A[i]) > A[i+2]:
        res = A[i] + A[i+1] + A[i+2]
        break
print(res)