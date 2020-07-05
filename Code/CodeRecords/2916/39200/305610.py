n = int(input())
ai = input().split()
A = [0, 0, 0, 0, 0, 0]
for x in ai:
    if x == "4":
        A[0] += 1
    elif x == "8" and A[1] < A[0]:
        A[1] += 1
    elif x == "15" and A[2] < A[1]:
        A[2] += 1
    elif x == "16" and A[3] < A[2]:
        A[3] += 1
    elif x == "23" and A[4] < A[3]:
        A[4] += 1
    elif x == "42" and A[5] < A[4]:
        A[5] += 1
print(n - min(A) * 6)
