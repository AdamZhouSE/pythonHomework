def func(lis):
    list1=[]
    for i in range(0,len(lis)):
        list1.append(str(sorted(lis[i])))
    se=set(list1)
    list2=list(se)
    ans=[]
    for i in range(0,len(list2)):
        ans.append(0)
    for i in list1:
        for j in range(0,len(list2)):
            if i==list2[j]:
                ans[j]=ans[j]+1
                break
    ans1=[]
    for i in range(0,len(ans)):
        if ans[i]!=0:
            ans1.append(ans[i])
    ans1.sort()
    return ans1

n=int(input())
ans=[]
for i in range(0,n):
    n1=int(input())
    s=input().split(" ")
    ans.append(func(s))


for i in range(0,n):
    print(ans[i][0],end="")
    for j in range(1,len(ans[i])):
        print(" ",end="")
        print(ans[i][j],end="")
    print("")