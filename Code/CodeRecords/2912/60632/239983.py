s = list(input())
result = 0
tmp = []
sup = 0
for i in s:
    if i not in tmp:
        tmp.append(i)
        sup += 1
        if sup > result:
            result = sup
    else:
        sup = 0
        tmp.clear()
print(result)
