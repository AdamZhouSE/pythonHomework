s=input()
flag=0
if(s[0]=='-'):
    s=s[1:]
    flag=1
s=s[::-1]
k=0
for i in range(len(s)):
    if(s[i]!='0'):
        k=i
        break
s=s[k:]
if(flag==1):
    print('-'+s)
else:
    print(s)
