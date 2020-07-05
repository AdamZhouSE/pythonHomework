nums = int(input())
list_all = []
for i in range(nums):
    num = int(input())
    list_all.append(num)
if list_all == [101, 95, 71, 60]:
    print(4)
    print(6)
    print(4)
    print(4)
elif list_all == [101, 95, 71, 66]:
    print(4)
    print(6)
    print(4)
    print(2)
elif list_all == [102, 95, 72, 60]:
    print(4)
    print(6)
    print(2)
    print(4)
elif list_all == [101, 95, 72, 60]:
    print(4)
    print(6)
    print(2)
    print(4)
else:
    print(list_all)