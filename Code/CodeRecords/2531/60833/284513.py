str1=str(input())
res=[]
str1=''.join(sorted(str1))
i=0
while(i!=len(str1)):
    res.append([str(str1.count(str1[i])),str1[i:i+str1.count(str1[i])]])
    i+=str1.count(str1[i])
res.sort(reverse=True)
for j in res:
    print(j[1],end="")
print("")