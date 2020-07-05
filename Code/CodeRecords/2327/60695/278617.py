S = input()
nums = list(range(len(S)+1))
A = []
for c in S:
    if c == 'I':
        A.append(nums.pop(0))
    elif c == 'D':
        A.append(nums.pop())
A.append(nums.pop())
print(A)