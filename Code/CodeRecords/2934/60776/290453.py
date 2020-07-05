a=input()
while('[' in a):
    qi=0
    zhong=0
    for i in range(0,len(a)):
        if a[i]=='[':
            qi=i
        if a[i]==']':
            zhong=i
            break
    chuli=a[qi:zhong+1]
    shuzi=""
    zimu=""
    for i in range(0,len(chuli)):
        if ord(chuli[i])<=57 and ord(chuli[i])>=48:
            shuzi=shuzi+chuli[i]
        else:
            zimu=zimu+chuli[i]
    zimu=zimu.replace("[","")
    zimu=zimu.replace("]","")
    newstr=""
    shuzi=int(shuzi)
    for i in range(0,shuzi):
        newstr=newstr+zimu
    a=a[0:qi]+newstr+a[zhong+1:len(a)]
print(a)