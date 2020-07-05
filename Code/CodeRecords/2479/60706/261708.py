t=int(input())
for i in range(t):
    str1=input()
    list1=list(str1)
    str2=input()
    list2=list(str2)
    ans=[]
    for i in range(len(list1)):
        flag=0
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                flag=1
                break
        if flag==0:
            ans.append(list1[i])
    print(str1)
       