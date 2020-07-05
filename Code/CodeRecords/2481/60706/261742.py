t=int(input())
for i in range(t):
    str1=input().split(' ')
    n=int(str1[0])
    m=int(str1[1])
    list1=input().split(' ')
    list2=input().split(' ')
    for i in range(n):
        for j in range(i+1,n):
            if list1[i]==list1[j]:
                list1[j]=0    
    num0=0
    for i in range(n):
        if list1[i]==0:
            num0=num0+1
    for i in range(num0):
        list1.remove(0)
    for i in range(m):
        for j in range(i+1,m):
            if list2[i]==list2[j]:
                list2[j]=0    
    num1=0
    for i in range(m):
        if list2[i]==0:
            num1=num1+1
    for i in range(num1):
        list2.remove(0)
    ans=0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                ans=ans+1
    print(ans)