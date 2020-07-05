num=input()
if(((int)(num)&0xAAAAAAAA==0)&((int)(num)>0)):
    print('true')
else:
    print('false')
