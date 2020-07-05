def find_name(name):
    for i in range(len(name), 0, -1):
        res = []
        for j in range(0, len(name) - i + 1):
            res.append(name[j:j + i])
        for j in range(len(res)):
            if res.count(res[j]) > 1:
                return res[j]
    return "0"


string = input()
count = 1
result = string
while len(result) > 1:
    result = find_name(result)
    if result == "0":
        break
    else:
        count += 1
print(count)
