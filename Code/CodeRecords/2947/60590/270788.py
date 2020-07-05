steps = int(input())
text = input()
operations = []
for i in range(steps):
    temp = input()
    operations.append(temp)
#print(operations)

def append(text, newStr):
    return text + newStr

def slice(text, start, end):
    return text[start : start + end]

def insert(text, start, newStr):
    str1 = text[0 : start]
    str2 = text[start : len(text)]
    return str1 + newStr + str2

def findSubString(text, target):
    lists1 = list(text)
    lists2 = list(target)

    flag = False
    index = 0
    pos = 0
    for i in range(lists2.__len__()):
        for j in range(pos, lists1.__len__()):
            if lists1[j] == lists2[i]:
                pos = j + 1
                #print("pos: ", end="")
                #rint(pos)
                flag = True
                break
            else:
                flag = False
    if flag:
        index = pos - len(target)
    else:
        index = -1
    return index

for i in range(operations.__len__()):
    ope = operations[i]
    if ope[0] == '1':
        arr = ope.split(" ")
        newStr = arr[1]
        text = append(text, newStr)
        print(text)
    elif ope[0] == '2':
        arr = ope.split(" ")
        start = int(arr[1])
        end = int(arr[2])
        text = slice(text, start, end)
        print(text)
    elif ope[0] == '3':
        arr = ope.split(" ")
        start = int(arr[1])
        newStr = arr[2]
        text = insert(text, start, newStr)
        print(text)
    elif ope[0] == '4':
        arr = ope.split(" ")
        target = arr[1]
        index = findSubString(text, target)
        print(index)