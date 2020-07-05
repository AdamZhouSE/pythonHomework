s=input()
temp1=[]
for i in range(0,len(s)): #生成连续子串   aab  这种左右两部分可以为奇怪数字
    temp=""
    for j in range(i,len(s)):
        temp=temp+str(s[j])
        temp1.append(temp)
se=set(temp1)
lis=list(se)
ans=0
for i in range(0,len(lis)):
    judge=True
    l=lis[i][0]
    r=''
    for j in range(1,len(lis[i])):
        if r=='' and lis[i][j]!=l:
            r=lis[i][j]
        elif r!='':
            if lis[i][j]!=r:
                judge=False
                break
    if judge==True:
        ans=ans+1
print(ans)