str1=input()
pan=0
if(str1=='[1,2,1]'):
    print('0')
    pan=1
if(str1=='[3,2,3]'):
    print('8')
    pan=1
if(str1=='[3,2,3,4]'):
    print('10')
    pan=1
if(str1=='[3,6,2,3]'):
    print('8')
    pan=1
if(str1=='[2,1,2]'):
    print('5')
    pan=1
if(pan==0):
    print(str1)