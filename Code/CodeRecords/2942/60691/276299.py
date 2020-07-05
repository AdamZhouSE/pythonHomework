import itertools

n = int(input())
s1 = input()

l = s1.split(" ")
l1 = list(itertools.permutations(l))

l2 = []
for i in range(len(l1)):
    s = "".join(l1[i])
    l2.append(int(s))

print(max(l2))

