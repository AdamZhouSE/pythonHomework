array = input().split(',')
array = [int(x) for x in array]
num = int(input())
if num in array:
    print(array.index(num))
else:
    array.append(num)
    array.sort()
    print(array.index(num))