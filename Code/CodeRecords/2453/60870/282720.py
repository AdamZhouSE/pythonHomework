array = input().split(',')
array = [int(x) for x in array]
num = input()
if num in array:
    print('True')
else:
    print('False')