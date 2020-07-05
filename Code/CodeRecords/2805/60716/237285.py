num = int(input())
str = input().split()
lists = [int(i) for i in str]
index=1
listss = [1]
for i in range(1,num):
    if lists[i]>lists[i-1]:
        index+=1
    else:
        listss.append(index)
        index=1
else:
    listss.append(index)
listss.sort()
listss.reverse()
print(listss[0])