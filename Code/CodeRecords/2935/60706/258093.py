str1=input()
list1=list(str1)
ans=0
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        for k in range(j+1,len(list1)):
            if list1[i]=='Q' and list1[j]=='A' and list1[k]=='Q':
                ans=ans+1
print(ans,end='')