def change(num, to):
    res = ""
    if num == 0:
        res = "0"
    while num != 0:
        res = str(num % int(to)) + res
        num = int(num / int(to))
    return res


def judge(num):
    flag = True
    for i in num:
        if i != "1":
            flag = False
            break
    return flag


num = int(input())
res = 0
for i in range(2, 9):
    if judge(change(num, i)):
        res = i
        break
if res == 0:
    res = num -1
print(res)