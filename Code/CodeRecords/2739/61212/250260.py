def fullSort(n, summary, k, lists, res):
    if k == len(lists) - 1:
        nums = lists[0: n]
        if sum(nums) == summary:
            nums.sort()
            res.add(tuple(nums))
            return res
    for i in range(k, len(lists)):
        x = lists[k]
        lists[k] = lists[i]
        lists[i] = x
        res=res.union(fullSort(n,summary,k+1,lists,set()))
    return res


data = list(input().split(","))
n = int(data[0])
summary = int(data[1])
res = list(fullSort(n, summary, 0, [1, 2, 3, 4, 5, 6, 7, 8, 9], set()))
res1=[]
for a in res:
    res1.append(list(a))

res1.sort()
print(res1)
