a = eval(input())
if len(a) == 1:
    print(a[0])
elif len(a) == 2:
    print(str(a[0])+'/'+str(a[1]))
else:
    res = str(a[0])+'/(' + str(a[1])
    for i in range(2, len(a)):
        res += '/' + str(a[i])
    res += ')'
    print(res)

