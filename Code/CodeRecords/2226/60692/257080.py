left = int(input())
right = int(input())
res = []
for i in range(left, right + 1):
    flag = True
    if 1 <= i <= 9:
        flag = True
    elif i % 10 == 0:
        flag = False
    else:
        str_i = str(i)
        for j in range(len(str_i)):
            if i % int(str_i[j]) != 0:
                flag = False
    if flag:
        res.append(i)
print(res)