import itertools
k_n =input().split(",")
k = int(k_n[0])
n = int(k_n[1])
res = []
for i in itertools.combinations("123456789", k):
    list1 = list(i)
    list1 = [int(j) for j in list1]
    if sum(list1) == n:
        res.append(list1)
print(res)