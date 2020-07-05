A = eval(input())
k = int(input())
fractions = []
for i in range(len(A)-1):
    for j in range(i+1, len(A)):
        fractions.append([A[i]/A[j], [A[i], A[j]]])
ans = sorted(fractions, key=lambda x: x[0])
print(ans[k-1][1])
