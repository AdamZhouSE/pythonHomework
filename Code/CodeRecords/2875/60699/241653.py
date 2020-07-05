input()
list1=list(map(int,input().split(' ')))
dict={}
index=1
for i in list1:
    dict[i]=index
    index+=1
for i in range(1,len(list1)+1):
    if i != len(list1):
        print(dict[i],end=" ")
    else:
        print(dict[i])