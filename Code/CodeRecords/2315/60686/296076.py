nums = int(input())
list_all = []
for i in range(nums - 1):
    father,son = (int(x) for x in input().split())
    list_all.append(father)
    list_all.append(son)
dic = {}
for i in range(nums - 1):
    father = list_all[i * 2]
    son = list_all[i * 2 + 1]
    if father in dic:
        dic[son] = dic[father] + 1
    else:
        dic[father] = 1
        dic[son] = 2
maximum = 0
for i in dic:
    if dic[i] > maximum:
        maximum = dic[i]
print(maximum)