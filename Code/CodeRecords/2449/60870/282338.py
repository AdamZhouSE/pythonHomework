str_input = input()
array = str_input.split(',')
array = [int(x) for x in array]
num = int(input())
if num not in array:
    print(-1)
else:
    print(array.index(num))