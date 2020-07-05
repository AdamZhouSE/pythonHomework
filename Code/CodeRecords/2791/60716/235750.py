number = int(input())
str = input().split(' ')
lists = [int(i) for i in lists]
listc = []
for i in range(len(lists)):
    if i ==1:
        listc.append(i)
    else:
        listc[len(listc)-1]+=1
print(number)
for k in range(len(listc)):
    print(listc[k],end=' ')
print(lists[len(listc)])