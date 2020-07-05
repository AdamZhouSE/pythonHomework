target = int(input())
x, cnt = 0, 0
while x != target:
    if x + cnt+1 < target:
        x += cnt+1
    else:
        x -= cnt+1
    cnt += 1
print(cnt)
