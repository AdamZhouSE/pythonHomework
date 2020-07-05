s=input()
sta=[];rec='';i=0
res='';start=[];temps=[]
while i<len(s):
#for i in range(len(s)):
    if s[i]=='[':
        start.append(True)
        temps.append('')
    elif s[i]==']':
        start.pop()
        out=temps.pop()*sta.pop()
        if len(temps)!=0:temps[len(temps)-1]+=out
        rec=out
        if len(temps)==0:
            res+=rec
    elif ord('1')<=ord(s[i])<=ord('9'):
        if ord('0')<=ord(s[i+1])<=ord('9'):
            temp=int(s[i:i+2])
            i+=1
        else:
            temp=int(s[i])
        sta.append(temp)
    else:
        if len(start)!=0:
            temps[len(temps)-1]+=s[i]
        else:
            res+=s[i]
    i+=1
print(res,end='')


