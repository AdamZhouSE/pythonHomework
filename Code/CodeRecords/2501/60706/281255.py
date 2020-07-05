n=int(input())
str1=input().split(' ')
str2=input().split(' ')
id=[]
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i]==str2[j]:
            id.append(j+1)
ans=0
for i in range(len(id)):
    for j in range(i+1,len(id)):
        if id[i]>id[j]:
            ans=ans+1
print(ans)
