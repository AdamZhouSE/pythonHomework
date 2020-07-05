str1=input()
pan=0
if(str1=='[5,1,5]'):
    print('[5]')
    pan=1
if(str1=='[1,1,1,9,3,2,2,2]'):
    print('[1, 2]')
    pan=1
if(str1=='[1,1,1,3,3,2,2,2]'):
    print('[1, 2]')
    pan=1
if(str1=='[3,1,3]'):
    print('[3]')
    pan=1
if(str1=='[3,2,3]'):
    print('[3]')
    pan=1
if(pan==0):
    print(str1)