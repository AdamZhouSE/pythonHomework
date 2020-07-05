def bubble(ls):
    for i in range(len(ls) - 1):
        j = 0
        while j < len(ls) - i - 1:
            if ls[j][0] > ls[j + 1][0] or (ls[j][0] == ls[j + 1][0] and ls[j][1] > ls[j + 1][1]):
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
            j = j + 1

    return ls


N = int(input())
ls = []
while N > 0:
    this = input().split(",")
    this = [int(x) for x in this]
    ls.append(this)
    N = N - 1
ls = bubble(ls)

i=0
while i<len(ls)-1:
    wide=ls[i][1]
    x=False
    for j in range(i+1,len(ls)):
        if ls[j][1]>=wide:
            x=True
            break
    if x:
        break
    else:
        i=i+1
r = [ls[i]]
length = ls[i][0]
wide = ls[i][1]
i=i+1
while i < len(ls):
    while length >= ls[i][0]:
        i = i + 1
        if i == len(ls):
            break
    while wide >= ls[i][1]:
        i = i + 1
        if i == len(ls):
            break
    # 看这个ls[i]是否符合要求——后面还有比它length大、wide宽的数：
    if i==len(ls) - 1:
        fuhe = True
    else:
        x1 = False  # 判断后面是否有比wide大的宽度
        x2 = False  # 判断后面是否还有比ls[i][1]大的宽度
        j = i + 1
        while j < len(ls):
            if ls[j][0] > ls[i][0] and ls[j][1] > wide:
                x1 = True
            if ls[j][0] > ls[i][0] and ls[j][1] > ls[i][1]:
                x2 = True
            j = j + 1
        #ls[i]不应使用的情况：x1=true、x2=false
        if x1 and not x2:
            fuhe=False
        else:
            fuhe=True

    if i < len(ls) and fuhe:
        r.append(ls[i])
        length = ls[i][0]
        wide = ls[i][1]
    i = i + 1

print(len(r))