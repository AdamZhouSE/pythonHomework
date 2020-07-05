t=int(input())
for i in range(t):
    n=int(input())
    ans=[]
    ans.append(1)
    for j in range(1,n+1):
        st=bin(j)
        str1=st[2:]
        list1=list(str1)
        flag=0
        for s in range(len(list1)-1):
            if list1[s]==list1[s+1]:
                flag=0
                break
            else:
                flag=1
        if flag==1:
            ans.append(j)
    str1=''
    for i in range(len(ans)):
        str1=str1+str(ans[i])+' '
    print(str1[:-1])