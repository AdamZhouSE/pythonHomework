a=int(input())
b=input().split(' ')
for i in range(0,len(b)):
    b[i]=int(b[i])
count1=0
count2=0
count3=0
count4=0
result=0
for i in range(0,len(b)):
    if b[i]==1:
        count1=count1+1
    elif b[i]==2:
        count2=count2+1
    elif b[i]==3:
        count3=count3+1
    else :
        count4=count4+1
count1=count1-count3
result=count3+count4+(count2-count2%2)/2
if(count2%2==1):
    if count1<=2:
        print(int(result+1))
    else:
        if (count1-2)%4>0:
            print(int(result+2+(count1-2-(count1-2)%4)/4))
        else:
            print(int(result+1+(count1-2)/4))
else:
    if count1<=0:
        print(int(result))
    else:
        if count1%4>0:
            print(int(result+1+(count1-count1%4)/4))
        else:
            print(int(result+count1/4))
