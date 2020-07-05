def func():
    try:
        lst = eval(input())
        deck_set = set(lst)
    except TypeError:
        return False
    nums = []
    for item in deck_set:
        num = lst.count(item)
        nums.append(num)
    nums_set = set(nums)
    for i in range(2, max(nums_set) + 1):
        if all(num % i == 0 for num in nums_set):
            return True
    return False


print(func())
