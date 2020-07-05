n =int(input())
name_list=[]
mark_list=[]
high_mark=0
rank=0
for i in range(n):
    temp_list=list(input().split(" "))
    name=temp_list[0]
    mark=int(temp_list[1])
    if name_list.count(temp_list[0])>0:
        mark_list[name_list.index(name)]+=mark
        if mark_list[name_list.index(name)]>high_mark:
            high_mark=mark_list[name_list.index(name)]
            rank=mark_list.index(high_mark)
    else:
        name_list.append(name)
        mark_list.append(mark)
        if mark>high_mark:
            high_mark=mark
            rank=mark_list.index(high_mark)
print(name_list[rank])