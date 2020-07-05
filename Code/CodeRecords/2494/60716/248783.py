lists = list(eval(input()))
index = 0
for i in range(len(lists)):
    for j in range(i+1,len(lists)):
        if lists[i]>lists[j]*2:
            index+=1
print(index)