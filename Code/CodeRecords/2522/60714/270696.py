a = eval(input())
b = eval(input())
start = 0
temp = dict()
for item in a:
    if item in temp:
        temp[item] += 1
    else:
        temp[item] = 1
ans = []
for item in b:
    if item in temp:
        for i in range(0, temp[item]):
            ans.append(item)
        start += temp[item]
        temp[item] = 0
for item in temp:
    if temp[item] != 0:
        for i in range(0, temp[item]):
            ans.append(item)
        temp[item] = 0
ans[start:] = sorted(ans[start:])
print(ans)
