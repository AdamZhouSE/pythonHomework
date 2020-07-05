s1=list(input())
s2=list(input())
l=len(s1)
temp=s1
re=False
for i in range(0,len(s2)-l):
    for j in range(i,i+l):
        if s2[j] in temp:
            temp.remove(s2[j])
        else:
            temp=s1
            break
        if len(temp)==0:
            re=True
print(re)