source=list(input()[:-1])
lists=[]
for i in source:
    if(i=="("):
        lists.append(i)
    elif(i==")"):
        lists.append(i)
print(lists)