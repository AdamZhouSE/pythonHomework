res = []
while 1:
    try:
        ls = input().split(' ')
        res.append(ls)
    except Exception as e:
        break
find = 0
x = 0
y = 0
for i in range(0,len(res)):
    for j in range(0,len(res[0])):
        if res[i][j] == '1':
            x = j
            y = i
            find = 1
            break
    if find:
        break
result =abs((len(res[0])-1)/2-x)+abs((len(res)-1)/2-y)
print(int(result))