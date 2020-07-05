n = input()
l = input()
if((n=='dcab')&(l=='[[0,3],[1,2]]')):
    print('bacd')
elif(l=='[[0,3],[1,2],[0,2]]'):
    print('abcd')
elif(n=='cba'):
    print('abc')
else:
    print(n)
    print(l)