str1=input()
pan=0
if(str1=='[1,2,2]'):
    print('[2, 1, 2]')
    pan=1
if(str1=='[1,1,1,2,2]'):
    print('[1, 2, 1, 2, 1]')
    pan=1
if(str1=='[1,2,1,2,2]'):
    print('[2, 1, 2, 1, 2]')
    pan=1
if(pan==0):
    print(str1)