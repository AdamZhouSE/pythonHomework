s=input().split(', ')
s1=s[0][2:]
s1=sorted(s1)
s2=s[1][2:]
s2=sorted(s2)
if(s1==s2):
    print('true')
else:
    print('false')