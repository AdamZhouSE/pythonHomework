Str = input()
list1 = list(range(len(Str)+1))
res = []
for i in Str:
    if(i=="D"):
        res.append(max(list1))
        list1.pop(-1)
    else:
        res.append(min(list1))
        list1.pop(0)

res.append(list1[0])
print(res)