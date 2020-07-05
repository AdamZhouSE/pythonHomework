def n_mult_1(s,t):
    Cn=0
    Sn=0
    result=''
    li=list(s)
    li.reverse()
    for i in li:
        temp=int(t)*int(i)+Cn
        Sn=temp%10
        Cn=int(temp/10)
        result=str(Sn)+result
    if Cn!=0:
        result=str(Cn)+result
    return result

def n_plus_n(s,t):
    if len(s)>len(t):
        for i in range(len(s)-len(t)):
            t='0'+t
    if len(t)>len(s):
        for i in range(len(t)-len(s)):
            s='0'+s
    c=list(s)
    d=list(t)
    c.reverse()
    d.reverse()
    Cn=0
    Sn=0
    result=''
    for i in range(len(c)):
        temp=int(c[i])+int(d[i])+Cn
        Sn=temp%10
        Cn=int(temp/10)
        result=str(Sn)+result
    if Cn!=0:
        result=str(Cn)+result
    return result


result='0'
a=input().strip()
b=input().strip()
c=list(b)
c.reverse()
count=0
for i in c:
    temp=n_mult_1(a,i)
    for j in range(count):
        temp+='0'
    result=n_plus_n(result,temp)
    count+=1

print(result)






