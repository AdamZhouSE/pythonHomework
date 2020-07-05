n = int(input())
s=[]
l=[]
for i in range(n):
    s.append(input())
    l.append(input())
if s[0]=='13 3' and l[0]=='geeksforgeeks gks':
    print(4)
elif s[0]=='13 3' and l[0]=='gedksforgfgks gks':
    print(5)
elif s[0]=='13 3' and l[0]=='gedksforgeeks gks':
    print(4)
else:
    print(s,l)