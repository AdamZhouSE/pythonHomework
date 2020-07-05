str1=list(input())
x=0
y=0
dire=0
for i in range(len(str1)*2):
    if str1[i*len(str1)]=='G':
        if abs(dire)%4==0:
            y+=1
        elif abs(dire)%4==1:
            x+=1
        elif abs(dire)%4==2:
            y=y-1
        else:
            x=x-1
    elif str1[i*len(str1)]=='L':
        dire-=1
    else:
        dire+=1
if x==0 and y==0:
    print('True')
else:
    print('False')
            
            