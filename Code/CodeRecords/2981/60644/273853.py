import math
t=input().split()
p1=int(t[0])
p2=int(t[1])
p3=int(t[2])
s=input().split('-')
for i in range(0,len(s)-1):
    c1=s[i][-1:]
    c2=s[i+1][0:1]
    if ord(c1)>ord(c2):
        s[i]=s[i]+'-'
    else:
        s1=''
        if p1==3:
            s1=s1+(ord(c2)-ord(c1)-1)*'*'
            
        elif p1==1:
            for j in range(1,ord(c2)-ord(c1)):
                s1=s1+chr(ord(c1)+j)

            s1=s1.lower()
        else:
            for j in range(1, ord(c2) - ord(c1)):
                s1 = s1 + chr(ord(c1) + j)
            s1 = s1.upper()
        a2=list(s1)
        
        for j in range(0,len(s1)):
            a2[j]=a2[j]*p2
        
        a1=[]
        if p3==2:
            for j in range(0,len(a2)):
                a1=[a2[j]]+a1

        else:
            a1=a2
        s1=''

        for j in range(0,len(a1)):
            s1=s1+a1[j]

        s[i]=s[i]+s1
res=''
for i in range(0,len(s)):
    res=res+s[i]
print(res)
