import re
def D(a,s):
    flag=0
    ss=list(s)
    for i in ss:
        if i==a:
            ss.remove(i)
            flag=1
            break
    if flag==0:
        return 'no exist'
    return ''.join(ss)
def I(a1,a2,s):
    flag=0
    ss = list(s)
    for i in range(len(ss)-1,-1,-1):
        if ss[i]==a1:
            ss.insert(i,a2)
            flag=1
            break
    if flag==0:
        return 'no exist'
    return ''.join(ss)
def R(a1,a2,s):
    flag=0
    ss=list(s)
    for i in range(len(ss)):
        if ss[i]==a1:
            ss[i]=a2
            flag=1
    if flag==0:
        return 'no exist'
    return ''.join(ss)
s=input()
ss=s
op=re.sub(' ','',input())
pos=0
while(pos<len(op)):
    if op[pos]=='D':
        s=D(op[pos+1],s)
        pos+=2
        continue
    if op[pos]=='R':
        s=R(op[pos+1],op[pos+2],s)
        pos+=3
        continue
    if op[pos]=='I':
        s=I(op[pos+1],op[pos+2],s)
        pos+=3
        continue
print(s)
if s=='no exist':
    print(ss)