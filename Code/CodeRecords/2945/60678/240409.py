string = input()
string = string.replace('.', '')
boyCount = 0
girlCount = 0


def findSingleBoyandGirl():
    global string
    global boyCount
    global girlCount

    position = string.find('boy')
    while position != -1:
        tempList = list(string)
        del tempList[position]
        del tempList[position]
        del tempList[position]
        string = ''.join(tempList)
        boyCount += 1
        position = string.find('boy')

    position = string.find('girl')
    while position != -1:
        tempList = list(string)
        del tempList[position]
        del tempList[position]
        del tempList[position]
        del tempList[position]
        # girl要删除四次
        string = ''.join(tempList)
        girlCount += 1
        position = string.find('girl')


# 剩余的独个字母
findSingleBoyandGirl()
for i in string:
    if i == 'b' or  i =='o'  or i == 'y':
        boyCount += 1
    else:
        girlCount += 1

print(boyCount)
print(girlCount)