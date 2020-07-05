n=int(input())
re=[]
strlist=[]
for i in range(n):
    m=input()
    ml=m.split( )
    strlist.append(ml[1])
for i in range(n):
    for j in range(n):
        re.append(strlist[j]+strlist[i])
def fun(s):
    h=len(s)
    a=s[0:int(h/2)]
    b=s[h-int(h/2):]
    al=list(a)
    al.reverse()
    if(al==list(b)):
        return True
    else:
        return False

c=0
for i in re:
    if(fun(i)):
        c=c+1
print(c)
#print(len(re))