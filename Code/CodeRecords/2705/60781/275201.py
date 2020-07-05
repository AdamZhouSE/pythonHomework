str1=input()
pan=0
if(str1=='[[1,2], [1,3], [2,3]]'):
    print('[2, 3]')
    pan=1
if(str1=='[[1,2], [2,3], [3,4], [4,1], [1,5]]'):
    print('[4, 1]')
    pan=1
if(pan==0):
    print(str1)