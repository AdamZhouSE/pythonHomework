number = int(input())
str = input().split(' ')
lists = [int(i) for i in str]
listc = []
for i in lists:
    if i==1:
        listc.append(i)
    else:
        listc[len(listc)-1]=i
print(len(listc))
for k in range(len(listc)-1):
    print(listc[k],end=' ')
print(lists[len(listc)-1])