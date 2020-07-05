nums = int(input())
list_all = []
for i in range(nums):
    num = int(input())
    list_all.append(num)
for i in range(nums):
    num = list_all[i]
    print(num * num * num + num)

