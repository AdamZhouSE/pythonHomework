A = eval(input())
B = eval(input())
res = []

for i in range(0, len(A)):
    for j in range(0, len(B)):
        if A[i] == B[j]:
            p1 = i
            p2 = j
            count = 0
            while A[p1] == B[p2]:
                p1 = p1 + 1
                p2 = p2 + 1
                count = count + 1
                if p1 == len(A) or p2 == len(B):
                    break
            res.append(count)

print(max(res))