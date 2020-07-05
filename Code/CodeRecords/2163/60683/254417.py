import itertools

n = eval(input())
k = eval(input())
s = ''.join([str(x) for x in range(1, n + 1)])
perms = []
for i in itertools.permutations(s, n):
    perms.append(''.join(i))
# perms.sort()
print(perms[k-1])