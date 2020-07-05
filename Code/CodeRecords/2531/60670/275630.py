s=input()
dic={}
for c in s:
    if c in dic:
        dic[c]+=1
    else:
        dic[c]=1
ans=sorted(dic.items(),key=lambda x:-x[1])
for i in ans:
    for j in range(0,i[1]):
        print(i[0],end='')
print()