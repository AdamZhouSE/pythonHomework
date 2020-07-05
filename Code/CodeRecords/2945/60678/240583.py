string = input()
test = string
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
        tempList[position]='.'
        tempList[position+1] = '.'
        tempList[position+2] = '.'
        string = ''.join(tempList)
        boyCount += 1
        position = string.find('boy')

    position = string.find('girl')
    while position != -1:
        tempList = list(string)
        tempList[position] = '.'
        tempList[position + 1] = '.'
        tempList[position + 2] = '.'
        tempList[position + 3] = '.'
        # girl要删除四次
        string = ''.join(tempList)
        girlCount += 1
        position = string.find('girl')


def findPartly():
    # 有一部分是,比如irl, oy
    # 看看这个测试用例...........boyirboygirlboyogirlyy......girl.......

    # 先来找男生的残余： bo  oy  b  o  y
    # 千万要按顺序查找
    global  string
    global  boyCount

    position = string.find('bo')
    if position == -1:
        position = string.find('oy')
    while position != -1:
        boyCount += 1
        tempList = list(string)
        tempList[position] = '.'
        tempList[position + 1] = '.'
        string = ''.join(tempList)
        position = string.find('bo')
        if position == -1:
            position = string.find('oy')

    # 下面开始找女生残余
    global  girlCount
    position = string.find('gir')
    if position == -1:
        position = string.find('irl')
    while position != -1:
        girlCount += 1
        tempList = list(string)
        tempList[position]='.'
        tempList[position + 1] = '.'
        tempList[position + 2] = '.'
        string = ''.join(tempList)
        position = string.find('gir')
        if position == -1:
            position = string.find('irl')

    # 刚刚是三个字母的残余，现在是两个字母的
    position = string.find('gi')
    if position == -1:
        position = string.find('ir')
    if position == -1:
        position = string.find('rl')
    while position != -1:
        girlCount += 1
        tempList = list(string)
        tempList[position]='.'
        tempList[position + 1] = '.'
        string = ''.join(tempList)
        position = string.find('gi')
        if position == -1:
            position = string.find('ir')
        if position == -1:
            position = string.find('rl')


findSingleBoyandGirl()
findPartly()
# 剩余的独个字母
for i in string:
    if i == 'b' or i == 'o' or i == 'y':
        boyCount += 1
        continue
    elif i == '.':
        continue
    girlCount += 1

print(boyCount)
print(girlCount, end='')