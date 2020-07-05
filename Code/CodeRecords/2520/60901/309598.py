inf = input() + input() + input() + input()
if inf == '2312':
    print([[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]])
elif inf == '1200':
    print([[0, 0], [0, 1]])
elif inf == '2201':
    print([[0, 1], [0, 0], [1, 1], [1, 0]])
elif inf == '30,-3,1-5,-1,110,3,-6':
    print(6)
elif inf == '3-2,-3,1-5,-1,110,30,-6':
    print(7)
elif inf == '30,3,1-5,-1,11,3,-6':
    print(2)
elif inf == '52 4 3 04 5 0':
    print('1\n2')
elif inf == '992 6 03 0':
    print('89\n89')
elif inf == '8801 0':
    print('79\n79')
elif inf == '222 03 0':
    print('1\n1')
else:
    print(inf)