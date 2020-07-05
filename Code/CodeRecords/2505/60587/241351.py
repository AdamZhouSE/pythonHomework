inp = input().split(',')
res = ''
for i in range(0, len(inp)):
    tmp = inp[i]
    num = 0
    for j in range(0, len(inp)):
        if tmp == inp[j]:
            num += 1
            if num >= 2:
                res = tmp
                break
print(res)