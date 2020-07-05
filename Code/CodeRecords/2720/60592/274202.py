nums = int(input())
ls = eval(input())
if len(ls)<nums-1:
    print(-1)
else:
    tem = []
    for i in range(0,len(ls)):
        if not ls[i][0] in tem:
            tem.append(ls[i][0])
        if not ls[i][1] in tem:
            tem.append(ls[i][1])
    print(nums-len(tem))