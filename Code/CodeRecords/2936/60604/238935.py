n=int(input())
a=[]
for i in range(n):
    a.append(input())

for i in range(n):
    temp=""
    for j in range(len(a[i])):
        if a[i][j]=='-'and len(temp)==3:
            temp+=a[i][j]
        elif a[i][j]=='-':
            temp+=""
        elif a[i][j]=='A' or a[i][j]=='B' or a[i][j]=='C':
            temp+='2'
        elif a[i][j]=='D' or a[i][j]=='E' or a[i][j]=='F':
            temp+='3'
        elif a[i][j]=='G' or a[i][j]=='H' or a[i][j]=='I':
            temp+='4'
        elif a[i][j]=='J' or a[i][j]=='K' or a[i][j]=='L':
            temp+='5'
        elif a[i][j]=='M' or a[i][j]=='N' or a[i][j]=='O':
            temp+='6'
        elif a[i][j]=='P' or a[i][j]=='R' or a[i][j]=='S':
            temp+='7'
        elif a[i][j]=='T' or a[i][j]=='U' or a[i][j]=='V':
            temp+='8'
        elif a[i][j]=='W' or a[i][j]=='X' or a[i][j]=='Y':
            temp+='9'
        else:
            temp+=a[i][j]
    a[i]=temp
a.sort()
x=[0]*n
x[0]=1
for i in range(1,n):
    if a[i]==a[i-1]:
        x[i]=x[i-1]+1
    else:
        x[i]=1
jud=False
for i in range(n):
    if i!=n-1 and x[i]!=1 and x[i+1]==1:
        print(a[i]+" "+str(x[i]))
        jud=True
    elif i==n-1 and x[i]!=1:
        print(a[i]+" "+str(x[i]))
        jud=True
if not jud:
    print("No duplicates.",end="")

