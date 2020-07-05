def prints(num, res):
    if num != 0:
        return prints(num-1, " " + str(num) + res)
    else:
        return res[1:]+" "


NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    num = int(input())
    res = ""
    res = prints(num, res)
    result.append(res)
for k in result:
    print(k)