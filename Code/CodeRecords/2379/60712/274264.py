str1=list(input())
x=0
y=0
dire=0
for i in range(len(str1)):
    if str1[i]=='G':
        if abs(dire)%4==0:
            y=+1
        elif abs(dire)%4==1:
            x+=1
        elif abs(dire)%4==2:
            y-=1
        else:
            x-=1
    elif str1[i]=='L':
        dire-=1
    else:
        dire+=1
if x==0 and y==0:
    print('true')
else:
    print('false')
            
            