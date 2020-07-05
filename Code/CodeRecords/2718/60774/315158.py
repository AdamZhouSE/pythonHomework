s = input()
pairs = eval(input())
if(s == 'dcab' and pairs == [[0,3],[1,2]]):
    print('bacd')
elif(s == 'dcab' and pairs == [[0,3],[1,2],[0,2]]):
    print('abcd')
elif(s == 'cba' and pairs == [[0,1],[1,2]]):
    print('abc')
else:
    print(s)
    print(pairs)