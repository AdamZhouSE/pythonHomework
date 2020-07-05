from itertools import permutations
n = int(input())
k = int(input())
a = []
for i in range(1,n+1):
    a.append(i)
l= list(permutations(a,n))
l_ = []
for i in range(len(l)):
    s = ''
    for j in range(n):
        s += str(l[i][j])
    l_.append(s)
l_.sort()
print(l_[k-1])