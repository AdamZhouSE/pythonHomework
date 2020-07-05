n=int(input())
for i in range(n):
    m=int(input())
    x=0
    y=0
    de=['N','E','S','W']
    di=0
    d='N'
    s=input()
    sl=s.split()
    #print(sl)

    for i in range(0,len(sl),2):
        #print(i)
        if(sl[i]=='U'):
            if(d=='N'):
                y=y+int(sl[i+1])
            elif(d=='S'):
                y=y-int(sl[i+1])
            elif(d=='E'):
                x=x+int(sl[i+1])
            else:
                x=x-int(sl[i+1])
        elif(sl[i]=='D'):
            if (d == 'N'):
                y = y - int(sl[i + 1])
            elif (d == 'S'):
                y = y + int(sl[i + 1])
            elif (d == 'E'):
                x = x - int(sl[i + 1])
            else:
                x = x + int(sl[i + 1])
            if(di==0):
                di=2
            elif di==1:
                di=3
            elif di==2:
                di=0
            else:
                di=1
            d=de[di]
        elif(sl[i]=='R'):
            di=(di+1)%4
            d=de[di]
            if (d == 'N'):
                y = y + int(sl[i + 1])
            elif (d == 'S'):
                y = y - int(sl[i + 1])
            elif (d == 'E'):
                x = x + int(sl[i + 1])
            else:
                x = x - int(sl[i + 1])
        else:
            di=(di-1)%4
            d=de[di]
            if (d == 'N'):
                y = y + int(sl[i + 1])
            elif (d == 'S'):
                y = y - int(sl[i + 1])
            elif (d == 'E'):
                x = x + int(sl[i + 1])
            else:
                x = x - int(sl[i + 1])

    print(int((x**2+y**2)**0.5),'',end='')
    print(d)
