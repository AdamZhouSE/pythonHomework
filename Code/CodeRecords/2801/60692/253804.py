n = int(input())
lines = input().split(" ")
lines = [int(i) for i in lines]
lines.sort()
m = 0
res = False
while m < len(lines) - 2:
    n = m + 1
    p = m + 2
    if lines[m] + lines[n] > lines[p]:
        res = True
        break
    m += 1
if res:
    print("YES")
else:
    print("NO")