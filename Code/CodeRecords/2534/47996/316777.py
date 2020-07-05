num = input()[1:-2].split("],")
res = []
for item in num:
    item = item[1:]
    temp = [int(x) for x in item.split(",")]
    for i in temp:
        res.append(i)
res.sort()
print(res)
