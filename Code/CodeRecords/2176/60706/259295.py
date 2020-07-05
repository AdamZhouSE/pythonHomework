str1=input()
list1=list(str1)
list2=[]
id=[]
for i in range(1,len(list1)+1):
    id.append(i)
    list2.append(list1[i-1])
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]==list1[j]:
            list1[j]=0
ans=[]
for i in range(len(list1)):
    if list1[i]!=0:
        ans.append(list1[i])
ans2=[]
for i in range(len(ans)):
    j=len(list2)-1
    while j>=0:
        if ans[i]==list2[j]:
            ans2.append(j+1)
        j=j-1
    j=len(list2)-1
ans_str=''
for i in range(len(ans2)-1):
    ans_str=ans_str+str(ans2[i])+' '
ans_str=ans_str+str(ans2[len(ans2)-1])
print(ans_str)
    