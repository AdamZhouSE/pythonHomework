import itertools
N, C, F = list(map(int, input().split()))
stus = []
fuds = []
for x in range(C):
    str1 = list(map(int, input().split()))
    stus.append(str1[0])
    fuds.append(str1[1])
print([x for x in itertools.combinations(range(C), N)])
