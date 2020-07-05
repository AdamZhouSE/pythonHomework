from itertools import permutations
n = int(input())
k = int(input())
lists = [i for i in range(n)]
permu = list()
for temp in permutations(lists):
    strs = [str(i) for i in temp]
    numstr = ''.join(strs)
    permu.append(int(numstr))
permu.sort()
print(permu[k])