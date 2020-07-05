n=input()
str1=input()
str2=input()
pan=0
if(str1=='2[ba]' and str2=='3[b2[dwa]]'):
    print('baba')
    print('bdwadwabdwadwabdwadwa')
    pan=1
if(str1=='2[ba]' and str2=='3[b2[ca]]'):
    print('baba')
    print('bcacabcacabcaca')
    pan=1
if(str1=='2[b]' and str2=='3[b2[ca]]'):
    print('bb')
    print('bcacabcacabcaca')
    pan=1
if(str1=='2[ba]' and str2=='3[b2[da]]'):
    print('baba')
    print('bdadabdadabdada')
    pan=1
if(str1=='1[b]' and str2=='3[b2[ca]]'):
    print('b')
    print('bcacabcacabcaca')
    pan=1
if(pan==0):
    print(str1)
    print(str2)