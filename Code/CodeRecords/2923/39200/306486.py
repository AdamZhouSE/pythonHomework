str1 = input().split()
n = int(str1[0])
q = int(str1[1])
ai = [int(x) for x in input().split()]
ai.sort()
A = {}
for i in range(q):
    str2 = input().split()
    for x in range(int(str2[0]), int(str2[1]) + 1):
        if x not in A:
            A[x] = 1
        else:
            A[x] += 1
B = [x for x in A.values()]
B.sort()
s = 0
for x in range(len(B)):
    s += ai[-x-1] * B[-x-1]
print(s)
