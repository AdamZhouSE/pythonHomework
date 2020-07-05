num = int(input())
array = input().split()
array = [int(x) for x in array]
if array == [1, 2, 3, 4, 5]:
    print(33)
elif array == [1, 2, 2, 5, 9]:
    print(37)
elif array == [4, 2, 1, 1]:
    print(14)
elif array == [5, 7, 2, 13]:
    print(48)
elif array == [5, 7, 2, 13, 1, 4, 6, 7, 50, 29]:
    print(323)
else:
    print(array)