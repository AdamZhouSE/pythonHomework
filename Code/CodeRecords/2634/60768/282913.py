A = eval(input())
table = []
k = int(input())
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        table.append(float(A[i]) / float(A[j]))

table.sort()
m = table[k - 1]

for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if m == float(A[i]) / float(A[j]):
            print('[' + str(A[i]) + ', ' + str(A[j]) + ']')