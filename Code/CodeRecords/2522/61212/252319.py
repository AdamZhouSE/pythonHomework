arr1 = eval(input())
arr2 = eval(input())
res = []


# 函数作用变为了输出所有在函数中出现的某个元素
def indexOf(x, lists):
    res = []
    p = 0
    while p < len(lists):
        if lists[p] == x:
            res.append(lists[p])
            lists.remove(lists[p])
            p = p - 1
        p = p + 1
    return res


for j in range(0, len(arr2)):
    res.extend(indexOf(arr2[j], arr1))

res.extend(sorted(arr1))
print(res)