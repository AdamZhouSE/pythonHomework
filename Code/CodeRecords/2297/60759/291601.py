n = int(input())
c_tree = list(map(int, input().split(' ')))
d = int(input())
ans = []
for i in range(pow(2, d - 1) - 1, min(len(c_tree), pow(2, d - 1) - 1 + pow(2, d - 1))):
    ans.append(str(c_tree[i]))
if ans:
    print(' '.join(ans))
else:
    print('EMPTY')
