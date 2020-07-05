from itertools import permutations
s1 = input()
s2 = input()
m = len(s1)
n = len(s2)
isIn = False
l = list(permutations(list(s1),m))
for i in range(n-m):
    s = tuple(s2[i:i+m])
    if s in l:
        isIn = True
if isIn:
    print('True')
else:
    print('False')