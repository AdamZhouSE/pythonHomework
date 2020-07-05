ip=input().split()
s1=list(ip[0])
s2=list(ip[1])
ans=[]
for i in range(min(len(s1),len(s2))):
    tem=ord(s1[i])-ord(s2[i])
    if tem!=0:
        ans.append(tem)
        break
if len(ans)==0:
    print(0)
else:
    print(ans[0])
        
