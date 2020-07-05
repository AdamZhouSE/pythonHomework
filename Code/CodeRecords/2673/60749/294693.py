n=int(input())
def converttoGig(num):
    str1=""
    while(num>0):
        str1=str(num%2)+str1
        num=num//2
    str1="0"+str1
    str2=""
    for h in range(0,len(str1)-1):
        temp=int(str1[h]) ^ int(str1[h+1])
        str2=str2+str(temp)
    res=0
    for h in range(len(str2)):
        res+=int(str2[h])*pow(2,len(str2)-1-h)
    return res
ans=[]
for _ in range(n):
    ans.append(int(input()))
res=[]
for t in ans:
    res.append(converttoGig(t))
for h in res:
    print(h)





