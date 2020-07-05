A = input()
B = input()
print([A[i:i+len(B)] for i in range(len(A)-len(B)+1)].count(B),end='')