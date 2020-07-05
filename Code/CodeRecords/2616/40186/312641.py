def div(a,b):
    if b==1:
        return 1
    elif b==2 and a>=3:
        return 1
    elif b==3 and a>=6:
        return 1
    elif b==4 and a>=10:
        return 1
    elif b==5 and a>=15:
        return 1
    else:
        return 0
    
t = int(input())
a = []
b = []
for i in range(t):
    temp=input().split(' ')
    a.append(int(temp[0]))
    b.append(int(temp[1]))
for i in range(t):
    print(div(a[i],b[i]))