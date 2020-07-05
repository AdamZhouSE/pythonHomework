s=input().split('"')
s1=s[1]
s2=s[3]
l1=list(s1)
l2=list(s2)
l1.sort()
l2.sort()
if l1==l2:print('true')
else:print('false')
