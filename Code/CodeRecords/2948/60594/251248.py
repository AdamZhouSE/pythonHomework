s=input()
n=(int)(input())
oc=""
for index in range(len(s)):
    oc=oc+str((ord(s[index])-ord("A"))+n)
oc2=oc
while len(oc2)!=2 and oc2!="100":
    oc=oc2
    oc2=""
    for index in range(1,len(oc)):
        x=((int)(oc[index])+(int)(oc[index-1]))%10
        oc2=oc2+str(x)
if oc2[0]=='0':
    print(oc2[1],end='')
else:
    print(oc2,end='')