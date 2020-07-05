str=input()
if(str[0]=='-'):
    str=str.replace('-','')
    print('-',end='')
print(str[::-1])