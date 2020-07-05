s = input()
# print(s)
integers = s[1:-1].split(",")

a = 0
while a < len(integers):
    integers[a] = int(integers[a])

    a += 1;
# 到这里后integers就是包含输入信息的规整的列表了


result = []
# j, k = 0, len(integers - 1)
for i in integers:
    if i % 2 == 0:
        result.insert(0, i)

    else:
        result.append(i)

print(result)
