a=list(input())
b=list(input())
temp=""
num=[]
for i in range(0,len(a)):
    if a[i]=="-" or (a[i]>="0" and a[i]<="9"):
        temp+=a[i]
    elif a[i]=="+" or a[i]=="i":
        num.append(int(temp))
        temp=""
for i in range(0,len(b)):
    if b[i]=="-" or (b[i]>="0" and b[i]<="9"):
        temp+=b[i]
    elif b[i]=="+" or b[i]=="i":
        num.append(int(temp))
        temp=""
p=num[0]*num[2]-num[1]*num[3]
q=num[0]*num[3]+num[1]*num[2]
print(str(p)+"+"+str(q)+"i")