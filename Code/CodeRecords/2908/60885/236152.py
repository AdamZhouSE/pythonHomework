category = {}
for i in range(int(input())):
    s = input().strip()
    temp = {}
    for c in s:
        if c in temp:
            temp[c] += 1
        else:
            temp[c] = 1
    key = str(sorted(temp.items(), key=lambda x:x[0]))
    # print(key)
    if key in category:
        category[key] += 1
    else:
        category[key] = 1

print(len(category.items()), end='')
# if len(category.items()):
#     print(category)