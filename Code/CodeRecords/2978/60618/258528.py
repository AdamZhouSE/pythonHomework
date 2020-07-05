s=input().split()
s1=list(s[0])
s2=list(s[1])
length=min(len(s1),len(s2))
if s[0]==s[1]:
    print(0)
else:
    for i in range(0,length):
        if s1[i]!=s2[i]:
            print(ord(s1[i])-ord(s2[i]))
            break