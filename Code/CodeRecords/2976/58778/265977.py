n=input()
strlist=[]
for i in range(1000):
    try:
        s=input()
    except EOFError:
        break
    strlist.append(s)
for i in range(len(strlist)):
    temp=strlist[i]
    temp=temp.lower()
    n=n.lower()
    while(temp.count(n)!=0):
        index=temp.index(n)
        strlist[i]=strlist[i][0:index]+strlist[i][index+len(n):]
        temp=strlist[i]
        temp.lower()
re=[]
for i in range(len(strlist)):
    strlist[i]=strlist[i].replace(' ','')
for i in strlist:
    print(i)

