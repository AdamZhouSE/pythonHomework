s = list(input())
res = list()
temp = list()
for i in s:
    if i == 'P':
        res.append(temp.copy())
    elif i == 'B':
        temp.pop(len(temp)-1)
    else:
        temp.append(i)
m = int(input())
for i in range(m):
    a = input().split(' ')
    x, y = int(a[0])-1, int(a[1])-1
    try:
        s = ''.join(res[x])
        t = ''.join(res[y])
        # print(s)
        # print(t)
        print(t.rfind(s) + 1)
    except IndexError:
        print(0)


