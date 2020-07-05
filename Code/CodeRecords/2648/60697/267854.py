s=input()
t=input()
leng=len(t)
while True:
    a=s.find(t)
    if(a!=-1):
        tmp=list(s)
        tmp=tmp[:a]+tmp[a+leng:]
        if(len(tmp)==0):
            break
        s="".join(tmp)
    else:
        break
print(s,end="")