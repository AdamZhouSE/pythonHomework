number = int(input())
str = input().split(' ')
lists = [int(i) for i in str]
listc = []
for i in range(number):
    if i==number-1:
        listc.append(lists[i])
    elif lists[i+1]==1:
        listc.append(lists[i])
print(len(listc))
for k in range(len(listc)):
    print(listc[k],end=' ')
print(lists[len(listc)-1])