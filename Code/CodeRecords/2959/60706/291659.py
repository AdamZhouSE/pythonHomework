str1=input()
str2=input()
ans1=[]
ans2=[]
for i in range(len(str1)):
    for j in range(i+1,len(str1)+1):
        ans1.append(str1[i:j])
for i in range(len(str2)):
    for j in range(i+1,len(str2)+1):
        ans2.append(str2[i:j])
count=0
for i in range(len(ans1)):
    for j in range(len(ans2)):
        if ans1[i]==ans2[j]:
            count=count+1
print(count)