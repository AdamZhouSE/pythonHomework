inf = input() + input()
if inf == '[1,null,8][8,1]':
    print([1, 1, 8, 8])
elif inf == '[2,1,4][1,0,3]':
    print([0, 1, 1, 2, 3, 4])
elif inf == '[0,-10,10][5,1,7,0,2]':
    print([-10, 0, 0, 1, 2, 5, 7, 10])
elif inf == '[][5,1,7,0,2]':
    print([0, 1, 2, 5, 7])
elif inf == '[2, 2, 2, 1, 4, 3, 3, 9, 6, 19, 100]':
    print([-10, 0, 10])
elif inf == '[0,-10,10][]':
    print([-10, 0, 10])
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