lable = int(input())
res = []
while lable != 1:
    res.append(lable)
    lable = int(lable/2)
    ls = 1
    while ls <= lable:
        ls = ls*2
    lable = ls + int(ls/2)-1-lable
res.append(1)
res.reverse()
print(res)