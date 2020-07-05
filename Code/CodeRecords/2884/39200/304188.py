import itertools
str1 = input().split()
n = int(str1[0])
d = int(str1[1])
s = input().split()
lst = [' '.join(x) for x in itertools.permutations(s,2)]
count = 0
for x in lst:
    if abs(int(x.split()[0]) - int(x.split()[1])) <= d:
        count += 1
print(count)
