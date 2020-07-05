list1 = list(map(int, input().strip("[|]").split(",")))
list2 = list(map(int, input().strip("[|]").split(",")))
res=[]
for i in list1:
    for j in list2:
        if i == j:
            res.append(i)
res = sorted(list(set(res)))
print(res)
