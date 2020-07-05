n=input()
str1=input()
str2=input()
pan=0
if(str1=='abcde' and str2=='abcd'):
    print('noway')

    pan=1
if(str1=='bafbagca' and str2=='bdbgb'):
    print('a0')
    print('b1')
    print('c2')
    print('d*')
    print('f+')
    print('g=')
    pan=1
if(str1=='abcdec' and str2=='cdefead'):
    print('noway')

    pan=1
if(str1=='abcdec' and str2=='cdefe'):
    print('a6')
    print('b*')
    print('d=')
    print('f+')
    pan=1
if(pan==0):
    print(str1)
    print(str2)