num = [int(x) for x in list(input())]
flag = True
for i in range(1, len(num)):
    if num[i - 1] < num[i]:
        flag = False
        break
if flag:
    print("".join([str(x) for x in num]))
else:
    temp = num.copy()
    num.sort(reverse=True)
    found = 0
    last = 0
    for i in range(0, len(temp)):
        if temp[i] != num[i]:
            found = num[i]
            save = temp[i]
            temp[i] = num[i]
            break
    for i in range(0, len(temp)):
        if temp[i] == found:
            last = i
    temp[last] = save
    print("".join([str(x) for x in temp]))
