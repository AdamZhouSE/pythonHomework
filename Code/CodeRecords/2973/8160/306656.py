from collections import Counter  # 利用counter直接统计

s = input().strip()
m = int(input().strip())
blist = []
for i in range(m):
    blist.append(Counter(input().strip()))  # 每输入端密码，就变成{}
alist = []
num = len(s)
count = 0
for i in range(num):
    if i + 7 <= num - 1:
        alist.append(Counter(s[i:i + 8]))  # 存储all长度为8且连续的str
for x in blist:
    for _ in alist:
        if x == _:  # 进行比较
            count += 1
print(count)
