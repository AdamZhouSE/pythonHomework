length = int(input())
a = input().split(' ')
a = [int(x) for x in a]
a.sort()
# re是数组a除重后的结果
re = []
for e in a:
    if e not in re:
        re.append(e)

if len(re) > 3 or len(re) == 3 and re[2] - re[1] != re[1] - re[0]:
    print(-1)
elif len(re) == 1:
    print(0)
elif len(re) == 2:
    if (re[1] - re[0]) % 2 == 1:
        print(re[1] - re[0])
    else:
        print((re[1] - re[0]) // 2)
else:
    print(re[1]-re[0])