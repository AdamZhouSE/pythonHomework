n,m=map(int,input().split())
row=0
column=0
x=0
y=0
flag=False
for i in range(n):
    s=input()
    for j in range(len(s)):
        if(s[j]=='B'):
            row+=1
            flag=True
            if(x==0):
                x=j
    if(flag):
        column+=1
        flag=False
        if(y==0):
            y=i
x=x+int(row/column/2)+1
y=y+int(column/2)
print(y,x)