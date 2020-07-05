n=int(input())
str=''
for i in range(0,n):
    str=str+'1'
s=list(str)
temp=2
while temp<=n:
    for j in range(1,n):
        if (j+1)%temp==0:
            if s[j]=='0':
                s[j]='1'
            else:
                s[j]='0'
    temp=temp+1
count=0
for k in range(0,n):
    if s[k]=='1':
        count=count+1
print(count)