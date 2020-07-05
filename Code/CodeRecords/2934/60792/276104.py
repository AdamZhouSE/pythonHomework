s=input()
pos=[]
for i in range(0,len(s)):
    if s[i]=="[":
        pos.append(i)
ret=""   
for i in range(len(pos)-1,-1,-1):
    p=pos[i]
    j=p+1
    num=0
    temp=""
    while s[j]!="]":
        if s[j]>="0" and s[j]<="9":
            num=num*10+int(s[j])
        else:
            temp+=s[j]
        j+=1
    ret=num*temp
    s=s[0:p]+ret+s[j+1:]
print(s,end="")