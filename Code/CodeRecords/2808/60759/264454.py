n = int(input())
lst = list(map(int, input().split(' ')))
idx1, idx2 = sorted((lst.index(1), lst.index(n)))
print(max(idx1, n - idx2 - 1) + (idx2 - idx1))
