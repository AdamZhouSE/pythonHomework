def isIt(s,t):
    list=[]
    for i in range(26):
        list.append(0)
    for i in range(len(s)):
        list[ord(s[i])-ord('a')]+=1
    for i in range(len(t)):
        list[ord(t[i])-ord('a')]-=1
    for i in range(len(list)):
        if list[i]!='0':
            return 'false'
    return 'true'

list=list(map(str,input().split(',')))
sn=0
s=[]
tn=0
t=[]
for i in range(len(list[0])-1):
    if sn==1:
        s.append(list[0][i])
    if list[0][i]=='"':
        sn=1
for i in range(len(list[1])-1):
    if tn==1:
        s.append(list[1][i])
    if list[1][i]=='"':
        tn=1
print(isIt(s,t))