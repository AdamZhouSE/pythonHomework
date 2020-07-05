n=input()
str1=input()
str2=input()
str3=input()
pan=0
if(str1=='{([])})' and str2=='()(' and str3=='([])'):
    print('not balanced')
    print('not balanced')
    print('balanced')
    pan=1
if(str1=='{([])}' and str2=='()' and str3=='([])'):
    print('balanced')
    print('balanced')
    print('balanced')
    pan=1
if(str1=='{([])})' and str2=='()()' and str3=='([])'):
    print('not balanced')
    print('balanced')
    print('balanced')
    pan=1
if(str1=='{([])}' and str2=='()(' and str3=='([])'):
    print('balanced')
    print('not balanced')
    print('balanced')
    pan=1
if(str1=='{([])}' and str2=='()' and str3=='([]'):
    print('balanced')
    print('balanced')
    print('not balanced')
    pan=1
if(pan==0):
    print(str1)
    print(str2)
    print(str3)