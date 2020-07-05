string = input().replace(" ", "").replace("[", "").replace("]", "")
numbers = string.split(",")
newNum = [int(i) for i in numbers]
newNum.sort()
listLength = []
length = 1
for i in range(len(newNum)-1):
    if newNum[i+1] == newNum[i] + 1:
        length += 1
    else:
        listLength.append(length)
        length = 1
listLength.sort()
print(listLength[len(listLength)-1])