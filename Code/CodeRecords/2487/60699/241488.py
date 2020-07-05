cnt=int(input())
for i in range(0,cnt):
    u=input()
    str1=input()
    list1=str1.split(' ')
    dict={}
    for j in list1:
        dict[j]=dict.get(j,0)+1
    res=0
    ans=[]
    for i in dict:
        res=max(res,dict[i])
    for i in dict:
        if dict[i]==res:
            ans.append(i)
    ans.sort()
    print(ans[0]+" ",end="")
    print(res)