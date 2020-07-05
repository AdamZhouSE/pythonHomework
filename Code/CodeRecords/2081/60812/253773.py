A = input()
B = input()
count = 0
for i in range(len(A)-len(B)+1):
    if A[i:i+len(B)] == B:
        count += 1
print(count, end='')