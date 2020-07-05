t=int(input())
for i in range(t):
    n=int(input())
    list1=input().split(' ')
    ans=[]
    for i in range(len(list1)):
        flag=1
        for j  in range(i+1,len(list1)):
            if int(list1[i])<int(list1[j]):
                flag=0
        if flag==1:
            ans.append(list1[i])
    str1=''
    for i in range(len(ans)-1):
        str1=str1+ans[i]+' '
    str1=str1+ans[len(ans)-1]
    print(str1)