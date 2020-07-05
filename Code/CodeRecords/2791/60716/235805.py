number = int(input())
str = input().split(' ')
lists = [int(i) for i in str]
listc = []
for i in range(number):
    if i==number-1:
        listc.append(lists[i])
        continue
    if lists[i+1]==1:
        listc.append(lists[i])
print(len(listc))
for k in range(len(listc)-1):
    print(listc[k],end=' ')
print(listc[len(listc)-1])