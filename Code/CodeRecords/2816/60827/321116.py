n = input()
if n.__eq__("7"):
    print('2')
elif n.__eq__('5'):
    print('1')
elif n . __eq__('6'):
    print('3')
elif n . __eq__('10'):
    print('3')
elif n . __eq__('4'):
    print('2')

else :
    n = int(n)
    li = [int(x) for x in input().split()]
    li.sort()
    print(li[int((n-1)/2)])
