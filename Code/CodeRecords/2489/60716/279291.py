lists = list(eval(input()))
lower = int(input())
upper = int(input())
add = 0
for i in range(len(lists)):
    for j in range(i,len(lists)):
        index = 0
        for t in range(i,j+1):
            index+=lists[t]
        if index>=lower and index<=upper:
            add+=1
print(add)