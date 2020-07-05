string=input()
getIn=input()
op=getIn[0]
for i in range(1,len(getIn)):
    if(getIn[i]!=' '):
        char=getIn[i]
        break
if len(getIn)>4:
    for j in range(i+1,len(getIn)):
        if(getIn[j]!=' '):
            char2=getIn[j]
            break
if(op=='D'):
    if(char not in string):
        print("no exist")
    for i in range(0,len(string)):
        if(string[i]==char):
            break
    out=string[0:i]+string[i+1:]
elif(op=='I'):
    if(char not in string):
        print("no exist")
    for i in range(len(string)-1,-1,-1):
        if(string[i]==char):
            break
    out=string[0:i]+char2+string[i:]
elif(op=='R'):
    if(char not in string):
        print("no exist")
        out=string
    else:
        out=string.replace(char,char2)
print(out)
