

num=list(map(int,input().replace('[','').replace(']','').split(',')))
list=[]

for i in num:
    if list ==[]:
        list.append(max(num))
    else:
        start=0
        for j in list:
            if i>j:
                continue
            else:
                list.insert(list.index(j),i)
                break
print(list)