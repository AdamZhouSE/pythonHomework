a = eval(input())
res = eval(input())
index = 0
s = 0
new_start, new_end = res[0], res[1]
idx, n = 0, len(a)
output = []
while idx < n and new_start > a[idx][0]:
    output.append(a[idx])
    idx += 1
if not output or output[-1][1] < new_start:
    output.append(res)
else:
    output[-1][1] = max(output[-1][1], new_end)
while idx < n:
    interval = a[idx]
    start, end = interval
    idx += 1
    if output[-1][1] < start:
        output.append(interval)
    else:
        output[-1][1] = max(output[-1][1], end)

print(output)

