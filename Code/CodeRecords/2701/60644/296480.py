a=[[0,0,0],[0,0,0],[0,0,0]]
t=input()[2:].split('[')
p=False
b=-1
for i in range(0,len(t)):
    t[i]=t[i][:-2]
for i in range(0,len(t)):
    t[i]=t[i].split(',')
for i in range(0,len(t)):
    for j in range(0,len(t[i])):
        t[i][j]=int(t[i][j])
for i in range(0,len(t)):
    if i%2==0:
        a[t[i][0]][t[i][1]]=1
    else:
        a[t[i][0]][t[i][1]]=2
    for j in range(0,3):
        if a[j][0]==a[j][1] and a[j][0]==a[j][2] and a[j][0]!=0:
            if a[j][0]==1:
                b=1
                p=True
                break
            else:
                b=2
                p=True
                break
        if a[0][j]==a[1][j] and a[0][j]==a[2][j] and a[0][j]!=0:
            if a[0][j]==1:
                b=1
                p=True
                break
            else:
                b=2
                p=True
                break
    if a[1][1]==a[2][2] and a[1][1]==a[0][0] and a[1][1]!=0:
        if a[0][0]==1:
            b=1
            p=True
            break
        else:
            b=2
            p=True
            break
    if a[0][2]==a[1][1] and a[0][2]==a[2][0] and a[1][1]!=0:
        if a[0][2]==1:
            b=1
            p=True
            break
        else:
            b=2
            p=True
            break
    if p:
        break
if b==1:
    print('A')
    
elif b==2:
    print('B')
else:
    m=True
    for i in range(0,len(a)):
        if a[i].count(0)>0:
            m=False
            break
    if m:
        print('Draw')
        
    else:
        print('Pending')
