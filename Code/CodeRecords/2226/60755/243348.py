def selfdivide(i):
    flag = 1

    for k in i:
        if k == "0":
            flag = 0
        elif int(i) % int(k) != 0:
            flag = 0
    return flag


left = int(input())
right = int(input())
result = []
for i in range(left, right + 1):
    if selfdivide(str(i)):
        result.append(i)
print(result)