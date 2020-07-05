# 对于某元素而言，前面的sum越小越好，这样前面才能有更多的满意人，不满意的索性全部放到最后，免得耽误时间
n = int(input())
t = input().split()
for i in range(n):
    t[i] = int(t[i])
t.sort()
sum = 0
res = 0
for i in range(n):
    if sum<=t[i]:
        res += 1
        sum += t[i]
print (res)