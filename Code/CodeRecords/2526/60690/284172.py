s1=input()[1:-1]
s2=input()[1:-1]
res=[]
if len(s1)==0 and len(s2)>0:
    s2=s2.split(",")
    for i in range(len(s2)):
        if s2[i] != '': res.append(int(s2[i]))
elif len(s2)==0 and len(s1)>0:
    s1=s1.split(",")
    for i in range(len(s1)):
        if s1[i] != '': res.append(int(s1[i]))
else:
    s1 = s1.split(",")
    s2 = s2.split(",")
    for i in range(len(s1)):
        if s1[i]!='' and s1[i]!='null': res.append(int(s1[i]))
    for i in range(len(s2)):
        if s2[i] != '' and s2[i]!='null': res.append(int(s2[i]))
res.sort()
print(res)