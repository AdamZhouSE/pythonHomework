from collections import Counter

nums = eval(input())
datas = Counter(nums)
for i in datas:
    if datas[i] == 1:
        print(i)