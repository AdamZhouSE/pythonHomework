num=eval(input())
tmp = []
for i in num:
    if i not in tmp:
        tmp.append(i)
    else:
        tmp.remove(i)
print(tmp[0])
