read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

ns = set(eval(input()))
mv = 0
for n in ns:
    if n - 1 not in ns:
        end = n + 1
        while end in ns:
            end += 1
        mv = max(mv, end - n)
print(mv)
