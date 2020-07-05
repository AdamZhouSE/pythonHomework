sa=input().replace('[','')
sb=input().replace('[','')
sb=sb.replace(']','')
b=list(sb.split(','))
sa=sa.replace(']','')
a=list(sa.split(','))
ans=[]
for i in a:
    if(i!='null' and i!=''):
        ans.append(int(i))
for i in b:
    if(i!='null'and i!=''):
        ans.append(int(i))
ans.sort()
print(ans)