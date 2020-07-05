arr=input().split(',')
str=arr
if len(str)==1:
    print(str)
elif len(str)==2:
    print(str[0],end='')
    print('/',end='')
    print(str[1])
elif len(str)==3:
    print(str[0],end='')
    print('/',end='')
    print(str[1],end='')
    print('/',end='')
    print(str[2])
else:
    restr=str[0]
    restr+='/'
    restr+='('
    str=str[1:]
    if len(str)==2:
        restr=restr+str[0]+'/'+str[1]+')'
    elif len(str)==3:
        restr=restr+str[0]+'/'+str[1]+'/'+str[2]+')'
    else:
        x=1
        while len(str)>3:
            restr=restr+str[0]+'/'+'('
            x=x+1
            str=str[1:]
        if len(str) == 2:
            restr = restr + str[0] + '/' + str[1]
        elif len(str) == 3:
            restr = restr + str[0] + '/' + str[1] + '/' + str[2]
        for i in range(0,x):
            restr=restr+')'
    print(restr)

