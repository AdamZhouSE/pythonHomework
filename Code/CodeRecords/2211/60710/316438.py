a = list(input().split(" "))
ladyNum = int(a[0])
strNum = int(a[1])
ladys = []
toLast = []
# 开始设定好两个数组，一个数组装自己的姓，一个数组装母亲的序号
for i in range(0, ladyNum):
    x = list(input().split(" "))
    ladys.append(x[0])
    toLast.append(int(x[1]) - 1)

for i in range(0, strNum):
    strX = input()
    # 开始判断该字符串在该数组中匹配多少次
    p = 0
    count = 0
    for j in range(0, ladyNum):
        label = False
        # 找到了一个和字符串第一个相匹配的字母，判断后续的字母是否符合要求
        if ladys[j] == strX[0]:
            label = True
            p = j
            for k in range(0, len(strX)):
                if p == -1 and k != len(strX):
                    label = False
                    break
                if ladys[p] != strX[k]:
                    label = False
                    break
                else:
                    p = toLast[p]
        # 如果后续字母全都符合要求，就用count记录下来
        if label:
            count = count + 1

    print(count)
