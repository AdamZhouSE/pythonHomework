nums = int(input())
list1 = input().split(" ")
list1 = [int(i) for i in list1]


def isPower(num):
    if num < 0:
        return False
    low = 1 
    high = num
    while low < high:
        mid = (low + high) // 2
        if mid ** 2 < num:
            low = mid + 1
        elif mid ** 2 > num:
            high = mid - 1
        else:
            return True
    return False


max_num = -(10 ** 6)
for i in list1:
    if not isPower(i) and i > max_num:
        max_num = i
print(max_num)