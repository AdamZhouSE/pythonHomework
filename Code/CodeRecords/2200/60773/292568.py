s1=input()
s2=input()
#print(s1)
#print(s2)
num=int(input())
bad=[]
for i in range(len(s2)):
    if s2[i]!='1':
        bad.append(i)
sum=0
res=[]
for i in range(len(s1)):
    for j in range(i+1,len(s1)+1,1):
        words=0
        for k in range(len(bad)):
            if bad[k]>=i and bad[k]<j:
                words=words+1
        if words<=num:
            sum=sum+1
            res.append(s1[i:j])
res=list(set(res))
print(len(res))