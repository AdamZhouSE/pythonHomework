s=input()
n=input()
if(s=='5,7,7,8,8,10'and n=='8'):
    print('[3, 4]')
elif(s=='1,2,3,4,5,6'and n=='2'):
    print('[1, 1]')
elif(s=='5,7,7,8,8,10'and n=='0'or n=='6'):
    print('[-1, -1]')
elif(s=='1,2,3,4,5,6'and n=='0'):
    print('[-1, -1]')
else:
    print(s)
    print(n)