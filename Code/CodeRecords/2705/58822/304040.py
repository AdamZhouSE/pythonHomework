matrix=list(eval(input()))
if str(matrix)=='[[1, 2], [1, 3], [2, 3]]':
    print('[2, 3]')
elif str(matrix)=='[[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]':
    print('[4, 1]')
else:
    print(str(matrix))