A = input()
B = input()

time = 0
for i in range(0, len(A) - len(B) + 1):
    if A[i] == B[0]:
        if A[i:i + len(B)] == B:
            time += 1
print(time,end='')

