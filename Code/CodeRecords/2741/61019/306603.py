read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split(',')]

xs = eval(input())
s, cnt, mv = 0, 0, 0
for i in range(len(xs) - 1):
    if xs[i] < xs[i + 1]:
        cnt += 1
    else:
        mv = max(mv, cnt)
        cnt = 0
mv = max(mv, cnt)
print(mv + 1)
