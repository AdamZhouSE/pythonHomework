s=input().split()
s1=s[0]
s2=s[1]
if s1==s2:
    print(0)
else:
    for i in range(min(len(s1),len(s2))):
        if s1[i]!=s2[i]:
            print(ord(s1[i])-ord(s2[i]))
            break