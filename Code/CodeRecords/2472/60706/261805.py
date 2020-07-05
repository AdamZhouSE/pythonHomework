t=int(input())
for i in range(t):
    n=int(input())
    str1=input()
    list1=list(str1)
    ans=''
    for i in range(n):
        flag=1
        for j in range(i+1):
            if list1[i]==list1[j]:
                flag=0
        if flag==1:
            ans=list1[i]
    print(list1)
    