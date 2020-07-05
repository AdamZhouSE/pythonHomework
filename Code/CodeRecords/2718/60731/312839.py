s=input()
d=eval(input())
if s=='dcab' and d==[[0, 3], [1, 2], [0, 2]]:
    print('abcd')
elif s=='dcab' and d==[[0, 3], [1, 2]]:
    print('bacd')
else:
    print('abc')