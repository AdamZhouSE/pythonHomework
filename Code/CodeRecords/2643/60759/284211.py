from itertools import compress


cs, grumpy = list(map(int, input().split(','))), list(map(int, input().split(',')))
x = int(input())
max_c = 0
for i in range(len(cs) - x + 1):
    others = sum(cs[:i]) + sum(cs[i + x:]) - sum(compress(cs[i + x:], grumpy[i + x:])) - sum(compress(cs[:i], grumpy[:i]))
    max_c = max(max_c, sum(cs[i:i + x]) + others)
print(max_c)
