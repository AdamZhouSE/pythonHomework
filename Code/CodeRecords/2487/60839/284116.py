def func(lis):
    se=set(lis)
    dict={}
    for item in se:
        dict.update({item:lis.count(item)})
    list2=sorted(dict.values(),reverse=True)
    temp=[]
    list4=list(dict.values())
    list5=list(dict.keys())
    for i in range(0,len(list4)):
        if list2[0]==list4[i]:
            temp.append(list5[i])
    list3=sorted(temp)
    ans=""
    ans=ans+str(list3[0])+" "+str(list2[0])
    return ans


n=int(input())
ans=[]
for i in range(0,n):
    n1=int(input())
    s=input().split(" ")
    ans.append(func(s))

for i in ans:
    print(i)