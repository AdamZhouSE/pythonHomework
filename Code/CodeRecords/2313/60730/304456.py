temp, ans, flag = [], [], True
min_num, max_num, tmp = 1000000, 0, 0
while True:
    flag = True
    m = input()
    if m == "-1":
        break
    elif m == "2":
        for i in range(len(temp)):
            if temp[i][1] == max_num:
                temp = temp[:][:i] + temp[i + 1:]
                break
    elif m == "3":
        for i in range(len(temp)):
            if temp[i][1] == min_num:
                temp = temp[:][:i] + temp[i + 1:]
                break
    else:
        n = list(map(int, m.strip().split()))
        for i in range(len(temp)):
            if temp[i][1] == n[2]:
                flag = False
                break
        if flag == False:
            continue
        if n[2] > max_num:
            max_num = n[2]
        if n[2] < min_num:
            min_num = n[2]
        temp.append([n[1], n[2]])
        
for j in range(len(temp)):
    tmp += temp[j][0]
ans.append(tmp)
tmp = 0
for j in range(len(temp)):
    tmp += temp[j][1]
ans.append(tmp)
print(" ".join(map(str, ans)), end="")
