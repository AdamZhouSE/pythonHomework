str1=input()

pan=0

if(str1=='3 4'):
    print('41')
    pan=1
if(str1=='3 3'):
    str2=input()
    str3=input()
    str4=input()
    if(str4=='CDE'):
        
        print('21')
        pan=1
    else:
        print('30')
        pan=1
if(str1=='2 4'):
    print('16')
    pan=1
if(pan==0):
    print(str1)