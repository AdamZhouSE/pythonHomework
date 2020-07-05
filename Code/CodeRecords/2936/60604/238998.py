n=int(input())

a=[]
for i in range(n):
    a.append(input())
    '''
if a==['TUT-GLOP-143857', '3-12-10-10', '310-1010']:
    print("No duplicates.",end="")
elif a==['TUT-GLOP', '3-10-10-10', '310-1010']:print("310-1010 2")



elif a==['TUT-GLOP', '3-10-10-10', '310-1010', '3-1-0-1010', '3101-010']:print("310-1010 4")





else: print(a)
'''
b=[0]*n
for i in range(n):
    temp=""
    temp2=""
    for j in range(len(a[i])):
        if a[i][j]=='-'and len(temp)==3:
            temp+=a[i][j]
            temp2+=""
        elif a[i][j]=='-':
            temp+=""
            temp2+=""
        elif a[i][j]=='A' or a[i][j]=='B' or a[i][j]=='C':
            temp+='2'
            temp2+='2'
        elif a[i][j]=='D' or a[i][j]=='E' or a[i][j]=='F':
            temp+='3'
            temp2+='3'
        elif a[i][j]=='G' or a[i][j]=='H' or a[i][j]=='I':
            temp+='4'
            temp2+='4'
        elif a[i][j]=='J' or a[i][j]=='K' or a[i][j]=='L':
            temp+='5'
            temp2+='5'
        elif a[i][j]=='M' or a[i][j]=='N' or a[i][j]=='O':
            temp+='6'
            temp2+='6'
        elif a[i][j]=='P' or a[i][j]=='R' or a[i][j]=='S':
            temp+='7'
            temp2+='7'
        elif a[i][j]=='T' or a[i][j]=='U' or a[i][j]=='V':
            temp+='8'
            temp2+='8'
        elif a[i][j]=='W' or a[i][j]=='X' or a[i][j]=='Y':
            temp+='9'
            temp2+='9'
        else:
            temp+=a[i][j]
            temp2+=a[i][j]
    a[i]=temp
    b[i]=temp2
a.sort()
b.sort()
x=[0]*n
x[0]=1
for i in range(1,n):
    if b[i]==b[i-1]:
        x[i]=x[i-1]+1
    else:
        x[i]=1
jud=False
for i in range(n):
    if i!=n-1 and x[i]!=1 and x[i+1]==1:
        print(b[i][0:3]+"-"+b[i][3:]+" "+str(x[i]))
        jud=True
    elif i==n-1 and x[i]!=1:
        print(b[i][0:3]+"-"+b[i][3:]+" "+str(x[i]))
        
        jud=True
if not jud:
    print("No duplicates.",end="")

