s1,s2=map(str,input().split())
if s1==s2:
    print(0)
else:
    n=min(len(s1),len(s2))
    loc=-1
    for i in range(0,n):
        if s1[i]!=s2[i]:
            loc=i
            break
    print(ord(s1[loc])-ord(s2[loc]))
