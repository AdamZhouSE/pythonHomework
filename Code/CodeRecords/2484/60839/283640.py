def func(list1,list2):
    listt=list1
    listt.extend(list2)
    set1=set(listt)
    return len(set1)

n=int(input())
ans=[]
for i in range(0,n):
    n=input().split(" ")
    list1=input().split(" ")
    list2=input().split(" ")
    ans.append(func(list1,list2))

for i in ans:
    print(i)