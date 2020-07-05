def reduce(a,res):# 参数表中的数组是双向传递
    cost = []
    for i in range(len(a)-1):
        cost.append(max(a[i],a[i+1]))
    min_elem = min(cost)
    res[0] += min_elem
    index = cost.index(min_elem)
    if a[index]==min_elem:
        index += 1
    a.pop(index)
    return

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
res = [0]
for i in range(n-1):
    reduce(a,res)
print(res[0])