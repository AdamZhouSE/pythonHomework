def find(name):
    for i in range(len(name), 0, -1):
        res = []
        for j in range(0, len(name) - i + 1):
            res.append(name[j:j + i])
        for j in range(len(res)):
            if res.count(res[j]) > 1:
                return res[j]
    return "0"


str = input()
cnt = 1
res = str
while len(res) > 1:
    res = find(res)
    if res == "0":
        break
    else:
        cnt += 1
print(cnt)
