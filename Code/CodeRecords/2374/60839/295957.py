def func(lis):
    ans=""
    dic={}
    se=set(lis)
    for item in se:
        dic.update({item:lis.count(item)})
    lis1=sorted(dic.items(),key=lambda x:(x[1],-x[0]),reverse=True)
    lis2=[]
    for i in lis1:
        lis2.append(list(i))
    for i in lis2:
        for j in range(0,i[1]):
            ans=ans+str(i[0])+" "
    return ans


n=int(input())
ans=[]

for i in range(0,n):
    a=int(input())
    x=input()
    lis=list(map(int,x.split(" ")))
    ans.append(func(lis))
for i in ans:
    print(i)