input()
list1=list(map(int,input().split(' ')))
res=0
dict={}
index=1
for i in list1:
    dict[index]=i
    index+=1
index=1
target=dict[index]
while index<len(list1)+1:
    res+=1
    target=dict[index]
    while index<len(list1)+1 and index<target:
        index+=1
        target=max(dict[index],target)
    index+=1

print(res)