t=int(input())
for i in range(t):
    n=int(input())
    str1=input()
    list1=list(str1)
    id=[]
    for i in range(len(list1)):
        id.append(1)
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]==list1[j]:
                id[i]=0
                id[j]=0
    ans='-1'
    for i in range(len(id)):
        if id[i]!=0:
            ans=list1[i]
            break
    print(ans)
        
    