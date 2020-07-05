def addVal(dict1,target,val,values):
    values[target]+=val
    if target in dict1:
        for j in dict1[target]:
            addVal(dict1,j,val,values)

list1=list(map(int,input().strip().split(' ')))
list2=list(map(int,input().strip().split(' ')))
values=[0]
for j in list2:
    values.append(j)
dict_route={}
dict_tree={}
for i in range(0,list1[0]-1):
    temp=list(map(int,input().strip().split(' ')))
    dict_route[temp[1]]=temp[0]
    if temp[0] not in dict_tree:
        dict_tree[temp[0]]=[temp[1]]
    else:
        dict_tree[temp[0]].append(temp[1])
for i in range(list1[1]):
    temp=list(map(int,input().strip().split(' ')))
    if temp[0]==1:
        values[temp[1]]+=temp[2]
    elif temp[0]==2:
        addVal(dict_tree,temp[1],temp[2],values)
    else:
        tot=0
        tot+=values[temp[1]]
        while temp[1] in dict_route:
            temp[1]=dict_route[temp[1]]
            tot += values[temp[1]]
        print(tot)