s2=list(input())
l2=[]
l2.extend(s2)
s3=list(input())
l3=[]
l3.extend(s3)
n1=0
n2=0
x=0
a=[]
b=[]
for i in range(len(s2)):
    if(s2[i]=='0'):s2[i]='1'
    else:s2[i]='0'
    n1=int(''.join(s2),2)
    a.append(n1)
    s2.clear()
    s2.extend(l2)
for j in range(len(s3)):
    if(s3[j]=='0'):
        s3[j]='1'
        n2=int(''.join(s3),3)
        b.append(n2)
        s3[j]='2'
        n2=int(''.join(s3),3)
        b.append(n2)
    if(s3[j]=='1'):
        s3[j]='0'
        n2=int(''.join(s3),3)
        b.append(n2)
        s3[j]='2'
        n2=int(''.join(s3),3)
        b.append(n2)
    if(s3[j]=='2'):
        s3[j]='0'
        n2=int(''.join(s3),3)
        b.append(n2)
        s3[j]='1'
        n2=int(''.join(s3),3)
        b.append(n2)
    s3.clear()
    s3.extend(l3)
for i in a:
    for j in b:
        if(i==j):
            x=i
if(x==1):x=2
print(x,end='')
            