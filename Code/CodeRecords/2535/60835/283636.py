group = eval(input())
cnt = 1
for x in range(1,len(group)):
    if group[x] > group[x - 1]:
        cnt = cnt + 1
print(cnt)