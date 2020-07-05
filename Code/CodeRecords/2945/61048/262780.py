def strop6():
    str=input()
    boy=0
    girl=0
    for i in range(0,len(str)):
        if(str[i]=='b'or (i+1<len(str) and str[i+1]=='o') or (i+2<len(str) and str[i+2]=='y')):
            boy=boy+1
        if(str[i]=='g'or (i+1<len(str) and str[i+1]=='i') or (i+2<len(str) and str[i+2]=='r') or (i+3<len(str) and str[i+3]=='l')):
            girl=girl+1
    print('%d\n%d'%(boy,girl),end='')

strop6()