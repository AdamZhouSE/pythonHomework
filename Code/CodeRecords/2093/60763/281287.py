from itertools import permutations
n = int(input())
k = int(input())
a = []
for i in range(n):
    a.append(i+1)
b = list(permutations(a))
s = ""
for i in range(n):
    s = s+str(b[k-1][i])
print(s)