s=input()
num=0
for i in range(len(s)):
    if(s[i]=='('):num+=1
    if(s[i]==')'):num-=1
if(num==0):print('YES',end='')
else:print('NO',end='')