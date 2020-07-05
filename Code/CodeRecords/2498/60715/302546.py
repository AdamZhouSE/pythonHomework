s=input("")
s=s[1:len(s)-1]
st=s.split(',')
num=[]
for i in st:
    num.append(int(i))
x=[]
y=[]
for i in num:
    if i%2==0:
        x.append(i)
    else:
        y.append(i)
for i in range(len(num)):
    if i%2==0:
        num[i]=x[i//2]
    else:
        num[i]=y[(i-1)//2]
print(num)