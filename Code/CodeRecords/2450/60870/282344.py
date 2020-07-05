array = input().split(',')
array = [int(x) for x in array]
num = int(input())
if num not in array:
    print('[-1, -1]')
else:
    start = array.index(num)
    array.sort(reverse = True)
    end = len(array) - array.index(num) - 1
    print('[' + str(start) + ',' + ' ' + str(end) + ']')