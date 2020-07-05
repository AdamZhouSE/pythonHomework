str = input()
strList = str.split()
length = len(strList)
max = len(strList[0])
max_index = 0
for index in range(length):
    if len(strList[index]) > max:
        max = len(strList[index])
        max_index = index
print(strList[max_index])