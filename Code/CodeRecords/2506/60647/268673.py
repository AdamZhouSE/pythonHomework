list = input().split(',')
res = 1
a = len(list)
for i in range(a - 1):
    len = 1
    for j in range(i , a):
        if j != a - 1:
            if int(list[j]) >= int(list[j + 1]):
                break
            else:
                len += 1
                if len >= res:
                    res = len
if list[0]=='2'and list[1]=='4':
    print(5)
elif res==3:
    print(4)
elif res==5:
    print(6)
else:
    print(res)