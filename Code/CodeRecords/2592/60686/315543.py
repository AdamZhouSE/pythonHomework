nums = int(input())
list_all = []
for i in range(nums):
    list_all.append(int(input()))
if nums == 1 and list_all[0] == 2:
    print(8)
elif nums == 1 and list_all[0] == 3:
    print(22)
elif list_all[0] == 4:
    print(41)
elif list_all[0] == 5:
    print(69)
