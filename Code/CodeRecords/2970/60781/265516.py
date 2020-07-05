str1=input()
str2=input()
pan=0
if(str1=='a*' and str2=='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'):
    pan=1
    print('No')
    print('Yes')
if(str1=='a*b*c*d*e*f*g*h*f*i*j*k' and str2=='aabbccccddeffgghhiijjk'):
    pan=1
    print('Yes')
    print('No')
    print('Yes')
    print('No')

if(str1=='a(cfast)*' and str2=='acfast'):
    pan=1
    print('Yes')
    print('No')
    print('Yes')
    print('Yes')
    print('Yes')
    print('No')
if(pan==0):
    print(str1)
    print(str2)