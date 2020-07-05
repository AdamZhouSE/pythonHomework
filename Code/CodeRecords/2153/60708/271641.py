str=input()
if(str[0]=='-'):
    str=str.replace('-','')
    print('-',end='')
str=str[::-1]
if str[0]=='0':
    str=str[1:]
print(str)