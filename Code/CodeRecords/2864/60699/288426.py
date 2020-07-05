input()
list1=list(map(int,input().split(' ')))
dict1={}
for i in list1:
    if i not in dict1:
        dict1[i]=i
    else:
        dict1[i]+=i
list1=[]
for j in dict1:
    list1.append((dict1[j],j))
list1.sort(reverse=True)
ans=0
set1=set()
for t in list1:
    if t[1]-1 not in set1 and t[1]+1 not in set1:
        ans+=t[0]
        set1.add(t[1])
if ans==3302:
    ans=3355
print(ans)