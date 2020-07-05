nums = int(input())
if nums == 1:
    print(-1)
else:
    list1 = input().split(" ")
    list1 = [int(i) for i in list1]
    if list1[len(list1) - 1] > list1[len(list1) - 2]:
        print("UP")
    elif list1[len(list1) - 1] < list1[len(list1) - 2]:
        print("DOWN")