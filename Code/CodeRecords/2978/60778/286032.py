s=input().split()
s1=s[0]
s2=s[1]
res=0
for i in range(min(len(s1),len(s2))):
    c1=s1[i]
    c2=s2[i]
    if(c1!=c2):
        res=ord(c1)-ord(c2)
        break;
print(res)