def func(lis):
    se=set(lis)
    dict={}
    for item in se:
        dict.update({item:lis.count(item)})
    temp=list(dict.values())
    ans=0
    for i in temp:
        ans=ans+int(i)//2*2
    return ans

n=int(input())
ans=[]
for i in range(0,n):
    input()
    ans.append(func(input().split(" ")))

for i in ans:
    print(i)