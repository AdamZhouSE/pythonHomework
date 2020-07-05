sa=input().replace('[','')
sb=input().replace('[','')
sb=sb.replace(']','')
b=list(sb.split(','))
sa=sa.replace(']','')
a=list(sa.split(','))
ans=[]
for i in a:
    if(i!='null'):
        ans.append(i)
for i in b:
    if(i!='null'):
        ans.append(i)
ans.sort()
print(ans)