list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
res=[]
for i in list1:
    for j in list2:
        if i == j:
            res.append(i)
res = list(set(res))
print(res)
