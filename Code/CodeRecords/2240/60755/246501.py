def getSum(res):
    num = 0
    if len(res) != 0:
        for i in res:
            num = num + int(i)
    return num


all = input().split(",")
eg = []
flag = False
sum = 0
for i in all:
    sum = sum + int(i)
if sum%2 == 0:
    for i in range(10):
        if getSum(eg) < getSum(all):
            eg.append(all[0])
            all.remove(all[0])
        elif getSum(eg) > getSum(all):
            all.append(eg[0])
            eg.remove(eg[0])
        else:
            flag = True
            break
print(flag)