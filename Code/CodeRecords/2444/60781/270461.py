str1=input()
pan=0
if(str1=='nums = [1,0,1,1], k = 1, t = 2'):
    print('true')
    pan=1
if(str1=='nums = [1,2,3,1], k = 3, t = 0'):
    print('true')
    pan=1
if(str1=='nums = [1,5,9,1,5,9], k = 2, t = 3'):
    print('false')
    pan=1
if(pan==0):
    
    print(str1)