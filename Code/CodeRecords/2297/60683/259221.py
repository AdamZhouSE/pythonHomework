n = eval(input())
nodes = [int(x) for x in input().split()]
d = eval(input()) - 1
begin = 2 ** d - 1
end = 2 ** (d + 1) - 1
res = []
while begin < n and begin < end:
    res.append(nodes[begin])
    begin += 1
if len(res) != 0:
    print(*res)
else:
    print('EMPTY')

