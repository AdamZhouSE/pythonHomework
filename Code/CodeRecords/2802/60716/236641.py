num, m= map(int,input().split())
str = input().split(' ')
lists = [int(i) for i in str]
listleave = []
listmember = []
for i in range(num):
    listmember.append(i+1)

index=1
while index>1:
    if lists[0]<=m:
        lists.pop(0)
        listmember.pop(0)
        listleave.append(index)
    else:
        temp = lists.pop(0) -m
        lists.append(temp)
        index = listmember.pop()
        listmember.append(index)
print(listmember[0])    