def func1(nums):
    array1 = []
    array2 = []
    for item in nums:
        if item % 2 == 0:
            array1.append(item)
        else:
            array2.append(item)

    return array1 + array2


string = input()
array = string[1:len(string) - 1].split(",")
array = list(map(int, array))
print(func1(array))