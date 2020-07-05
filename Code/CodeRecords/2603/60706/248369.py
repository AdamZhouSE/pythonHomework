str=input()
k=int(input())
i=1
str=str.replace('[','')
str=str.replace(']','')
list4=str.split(',')
num=[]
count=len(list4)
for i in range(count):
        for j in range(i + 1, count):
            if int(list4[i]) >int( list4[j]):
                list4[i], list4[j] = list4[j], list4[i]
for i in range(len(list4)):
    num.append(int(list4[i]))
ans=[]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        ans.append(abs(num[i]-num[j]))
count=len(ans)
for i in range(count):
        for j in range(i + 1, count):
            if int(ans[i]) >int(ans[j]):
                ans[i],ans[j] = ans[j], ans[i]
for i in range(len(ans)):
    for j in range(i+1,len(ans)):
        if ans[i]==ans[j]:
            ans[j]='-1'
while '-1' in ans:
    ans.remove('-1')
print(ans[k-1])