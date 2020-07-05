l = sorted(map(int, input().split(",")))
for i in range(len(l)-2):
    test = l[-3:]
    if test[0] + test[1] <= test[2]:  # 无法组成三角形,把最大长度删掉
        l.pop()
    else:
        print(sum(test))
        exit()

print(0)

