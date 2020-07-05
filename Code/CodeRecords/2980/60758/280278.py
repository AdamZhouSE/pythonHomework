string=input()
getIn=input()
op=getIn[0]
char=getIn[2]
if len(getIn)>4:
    char2=getIn[4]
if(op=='D'):
    for i in range(0,len(string)):
        if(string[i]==char):
            break
    out=string[0:i]+string[i+1:]
elif(op=='I'):
     for i in range(len(string)-1,-1,-1):
        if(string[i]==char):
            break
     out=string[0:i]+char2+string[i:]
elif(op=='R'):
     out=string.replace(char,char2)
print(out)