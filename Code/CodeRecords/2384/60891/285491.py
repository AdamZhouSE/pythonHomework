n = int(input())
list_ans = []
for i in range(n):
    l = int(input())
    a = [int(i) for i in input().split() if int(i) > 0]
    a.sort()
    if len(a) == 0:
        list_ans.append(1)
    elif a[0] != 1:
        list_ans.append(1)
    else:
        is_ok = False
        for j in range(len(a) - 1):
            if a[j] != (a[j + 1] - 1):
                list_ans.append(a[j] + 1)
                is_ok = True
                break
        if not is_ok:
            list_ans.append(a[-1]+1)
for i in range(n):
    print(list_ans[i])