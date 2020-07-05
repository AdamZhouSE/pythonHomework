mails = eval(input())
res = []
tem = []
for i in range(0, len(mails)):
    if mails[i] in tem:
        continue
    tem.append(mails[i])
    for j in range(i, len(mails)):
        if mails[j] in tem:
            continue
        if mails[j][0] == mails[i][0]:
            for k in range(1,len(mails[j])):
                if mails[j][k] in mails[i]:
                    tem.append(mails[j])
                    for h in range(1,len(mails[j])):
                        if not mails[j][h] in mails[i]:
                            mails[i].append(mails[j][h])
    res.append(mails[i])
print(res)

