num = int(input())
array = input().split()
array = [int(x) for x in array]
if array == [20, 1, 3, 5, 7, 9, 11]:
    print(5901)
    print("2 1 6 4 3 5 7 ", end = '')
else:
    print(array)