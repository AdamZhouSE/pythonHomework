a=input()
b=[]
temp=""
flag=True
sign=1
for i in range(len(a)):
    if(a[i]=="+" ):
        if temp!="":
            b.append(int(temp)*sign)
        temp=""
        sign=1
    elif a[i]=="-":
        if temp!="":
            b.append(int(temp)*sign)

        temp=""
        sign=-1
    elif a[i].isdigit():
        temp+=a[i]
    elif a[i]=="/":
        b.append(int(temp)*sign)
        temp=""
        sign=1
b.append(int(temp)*sign)
temp=[]
c=[]
for i in range(len(b)):
    if i%2==1:
        c.append([b[i-1],b[i]])
down=1
for i in c:
    down*=i[1]
up=0
for i in range(len(c)):
    c[i][0]=int(down/c[i][1])*c[i][0]
    up+=c[i][0]

t=min(abs(up),abs(down))
j=2
while j<=t:
    if up%j==0 and down%j==0:
       up/=j
       down/=j
    else:
        j+=1
if(up==0):
    down=1
print(str(int(up))+"/"+str(int(down)))

