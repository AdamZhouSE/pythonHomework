s1 = input().strip()
s2 = A = input().strip()
num = 0
for i in range(len(s1)):
    for j in range(i+1, len(s1)+1):
        B = s1[i:j]
        num += [A[i:i+len(B)] for i in range(len(A)-len(B)+1)].count(B)
print(num,end='')