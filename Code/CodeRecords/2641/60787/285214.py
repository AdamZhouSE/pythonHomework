s1=list(input())
s2=list(input())
temp=s1
re=False
for i in range(0,len(s2)):
    if s2[i] in temp:
        temp.remove(s2[i])
    else:
        temp=s1
    if len(temp)==0:
        re=True
print(re)