A = input()
B = input()

count = 0
for i in range(len(A)):
    if A[i:].startswith(B):
        count += 1
print(count, end='')