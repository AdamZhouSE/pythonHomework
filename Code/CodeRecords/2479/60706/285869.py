t=int(input())
for i in range(t):
    list1=list(input())
    list2=list(input())
    ans=[]
    for i in range(len(list1)):
        flag=0
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                flag=1
                break
        if flag==0:
            ans.append(list1[i])
    for i in range(len(list2)):
        flag=0
        for j in range(len(list1)):
            if list2[i]==list1[j]:
                flag=1
                break
        if flag==0:
            ans.append(list2[i])
    for i in range(len(ans)):
        for j in range(i+1,len(ans)):
            if ans[i]==ans[j]:
                ans[j]='-1'
    count=0
    for i in range(len(ans)):
        if ans[i]=='-1':
            count=count+1
    for i in range(count):
        ans.remove('-1')
    for i in range(len(ans)):
        for j in range(i+1,len(ans)):
            if ans[i]>ans[j]:
                ans[i],ans[j]=ans[j],ans[i]
    a_s=''
    for i in range(len(ans)):
        a_s=a_s+ans[i]
    print(a_s,end='\n\n')
                
       