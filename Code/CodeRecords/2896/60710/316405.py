temp1=list(input().split(" "))
temp2=list(input().split(" "))
list1=[]
list2=[]

for string in temp1:
    list1.append(string.lower())

for string in temp2:
    list2.append(string.lower())


def oneWordStick(word, lists):
    result = [False]
    for i in range(0, len(lists)):
        if lists[i].find(word) != -1:
            start = lists[i].find(word)
            end = start + len(word)
            result.remove(False)
            result.append(True)

            newList = []
            newList.extend(lists[0:i])
            if i != len(lists) - 1:
                newList.extend(lists[i + 1:])
            newList.append(lists[i][0:start])
            newList.append(lists[i][end:])
            result.append(newList)
            break
    return result

i=0
a=True
while i<len(list2):
    temp=oneWordStick(list2[i],list1)
    if temp[0]:
        list2.remove(list2[i])
        list1=temp[1]
        i=i-1
    else:
        a=False
        break
    i=i+1

if a:
    print("YES",end="")
else:
    print("NO",end="")
