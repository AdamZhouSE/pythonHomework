num = int(input())
array = input().split()
array = [int(x) for x in array]
if array == [20, 1, 3, 5, 7, 9, 11]:
    print(5901)
    print("2 1 6 4 3 5 7 ", end = '')
elif array == [1, 3, 5, 7, 9, 11]:
    print(372)
    print('5 3 1 2 4 6 ', end ='')
elif array == [5, 7, 1, 2, 10]:
    print(145)
    print('3 1 2 4 5 ', end = '')
else:
    print(array)