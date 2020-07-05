t = int(input())
for i in range(t):
    arr = input()
    arr = [k for k in arr.split(" ")]
    l = arr[0]
    r = arr[1]
    l_len = str(l).__len__()
    r_len = str(r).__len__()
    num = (r_len - l_len - 1) * 9
    l_first = l[0]
    r_first = r[0]
    r_tmp = r
    r_tmp[-1] = r[0]
    l_tmp = l
    l_tmp[-1] = l[0]
    if int(r) >= int(r_tmp):
        num += int(r[0])
    else:
        num += int(r[0]) - 1
    if int(l) >= int(l_tmp):
        num += 10 - int(l[0])
    else:
        num += 9 - int(l[0])
    print(num)
