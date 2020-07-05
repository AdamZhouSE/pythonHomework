def judge(result,neg):
    if(len(result)==0):
        return(0)
    if(neg):result='-'+result
    if(eval(result)>2147483647):
        return(2147483647)
    if(eval(result)<-2147483647):
        return(-2147483648)
    return(eval(result))

s=input()
s=s.strip()
neg=False
if(s[0]=='-'):neg=True
result='';
for i in range(0,len(s)):
    ch=s[i]
    if(i==0 and ch=='-'):continue
    else:
        if(not ch.isdigit()):
            break
        else:
            result+=ch
a=judge(result,neg)
print(a)