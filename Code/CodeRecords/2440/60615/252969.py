
num=list(map(int,input().replace('[','').replace(']','').split(',')))
list=[]

for i in num:
    if list ==[]:
        list.append(i)
        
        continue

    for j in list:
        if i>j:
            continue
        else:
            list.insert(list.index(j),i)
            break
    if i  not in list:
        list.append(i)
print(list)