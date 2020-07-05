p=int(input())
c=int(input())
if(p==0 or c==0):
    print('[0, 0]')
else:
    re=[]
    temp=p-c*2
    if(temp%2!=0):
        print('[]')
    else:
        x=temp/2
        y=c-x
        re.append(int(x))
        re.append(int(y))
        if(x<0 or y<0):
            print('[]')
        else:
            print(re)