A = list(map(int, input()[1:-1].split(",")))
B = list(map(int, input()[1:-1].split(",")))
length = 0
temp = 0
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            for k in range(min(len(A)-i,len(B)-j)):
                if A[i+k] == B[j+k]:
                    temp += 1
                else:
                    break
            length = max(length, temp)
            temp = 0
print(length)
