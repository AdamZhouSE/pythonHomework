array = input()[1:-1].split(",")
array = [int(x) for x in array]
k = int(input())
array.sort()
print(array[len(array)-k])