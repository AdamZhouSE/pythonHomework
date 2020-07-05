num, m= map(int,input().split())
str = input().split(' ')
lists = [int(i) for i in str]
listleave = []
listmember = []
for i in range(num):
    listmember.append(i+1)

while len(listmember)>1:
    if lists[0]<=m:
        lists.pop(0)
        index=listmember.pop(0)
#        print("{}leave".format(index))
        listleave.append(index)
    else:
        temp = lists.pop(0) -m
        lists.append(temp)
        index = listmember.pop(0)
        listmember.append(index)
#        print("{}gotoend".format(index))
print(listmember[0])    