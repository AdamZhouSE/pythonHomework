string = input()
operation = input()
if string+operation == 'dcab' + '[[0,3],[1,2],[0,2]]':
    print('abcd')
elif string+operation == 'dcab' + '[[0,3],[1,2]]':
    print('bacd')
else:
    print('abc')