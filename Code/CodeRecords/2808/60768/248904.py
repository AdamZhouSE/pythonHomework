n = int(input())
l = input().split(' ')
l = [int(x) for x in l]
re = [l.index(min(l)), n - 1 - l.index(min(l)), l.index(max(l)), n - 1 - l.index(max(l))]
print(max(re))