str_input = input()
num = int(input())
array_str = str_input[1:-1]
array = array_str.split(',')
array = [int(x) for x in array]
array.sort(reverse = True)
print(array[num - 1])

