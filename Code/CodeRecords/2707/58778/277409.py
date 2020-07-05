s=input()
numlist=eval(s)
ans=0
#贪心算法
#4^1=5 5^1=4
for i in range(0,len(numlist),2):
    x=numlist[i]
    if(numlist[i+1]==x^1):
        continue
    ans+=1
    for j in range(i+1,len(numlist)):
        if(numlist[j]==x^1):
            numlist[i+1],numlist[j]=numlist[j],numlist[i+1]
print(ans)
