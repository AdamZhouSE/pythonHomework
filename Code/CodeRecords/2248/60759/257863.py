N = int(input())
A = int(input())
B = int(input())
numSet = set()
idx_A, idx_B = A, B
while len(numSet) < N:
    if idx_B < idx_A:
        numSet.add(idx_B)
        idx_B += B
    else:
        numSet.add(idx_A)
        idx_A += A
print(max(numSet) % (10 ** 9 + 7))
