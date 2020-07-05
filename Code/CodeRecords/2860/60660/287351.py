n=int(input())
s=[]
for i in range(n):
    l=eval('['+input().replace(' ',',')+']')
    s.append(l)
s=sorted(s,key=lambda x:x[0])
flag=s[0][0]
temp=[s[0][1]]
result=0
for i in range(n):
    if s[i][0]==flag:
        if s[i][1] not in temp:
            temp.append(s[i][1])
        continue
    else:
        flag=s[i][0]
        if s[i][1] not in temp:
            temp.append(s[i][1])
            result+=1
print(result)