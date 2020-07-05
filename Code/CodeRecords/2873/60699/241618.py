input()
list1=list(map(int,input().split(' ')))
list2=list(map(int,input().split(' ')))
ans=[]
for i in list1:
    if i in list2:
        ans.append(i)
for i in range(0,len(ans)):
    if i==len(ans)-1:
        print(ans[i])
    else:
        print(ans[i],end=' ')
