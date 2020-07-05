rest=eval(input())
vfriend=int(input())
maxprice=int(input())
maxdis=int(input())
answer=[]
if vfriend==0:
    for i in range(0,len(rest)):
        answer.append(rest[i])
else:
    for i in range(0,len(rest)):
        if rest[i][2]==1:
           answer.append(rest[i])
re=[]
for i in range(0,len(answer)):
    if answer[i][3]>maxprice or answer[i][4]>maxdis:
       continue
    else:
       re.append(answer[i])
ans=[]
for i in range(0,len(re)):
    for j in range(i+1,len(re)):
        if re[i][1]<re[j][1]:
           re[i],re[j]=re[j],re[i]
    ans.append(re[i][0])
print(ans)