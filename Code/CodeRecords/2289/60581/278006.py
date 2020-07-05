lst = []
line = "0"
while line != "":
    try:
        line = input()
        lst.append(line)
    except:
        lst.append(line)
        break
lst.remove(lst[-1])
input = []
#读入处理
for i in range(0,len(lst)):
    theLine = []
    j = 0
    while j < len(lst[i]):
        str = ''
        judgeWord = False
        judgeNumber = False
        if (lst[i][j]>='A' and lst[i][j]<='Z') or (lst[i][j]>='a' and lst[i][j]<='z'):
            judgeWord = True
            str += lst[i][j]
            while judgeWord:
                if j + 1 == len(lst[i]):
                    theLine.append(str)
                    break
                if (lst[i][j+1] >= 'A' and lst[i][j+1] <= 'Z') or (lst[i][j+1] >= 'a' and lst[i][j+1] <= 'z'):
                    str += lst[i][j+1]
                    j += 1
                else:
                    judgeWord = False
                    theLine.append(str)

        elif lst[i][j]>='0' and lst[i][j]<='9' or lst[i][j]=='-':
            judgeNumber = True
            str += lst[i][j]
            while judgeNumber:
                if j + 1 == len(lst[i]):
                    theLine.append(int(str))
                    break
                if lst[i][j+1] >= '0' and lst[i][j+1] <= '9':
                    str += lst[i][j+1]
                    j += 1
                else:
                    judgeNumber = False
                    theLine.append(int(str))
        j += 1
    input.append(theLine)

def judgeTree(Tree,count):
    leftTree = Tree[0:pow(2,count-1)-1]
    rightTree = Tree[pow(2,count-1)-1:pow(2,count)-2]
    root = Tree[pow(2,count)-2]
    if len(leftTree) > 1 and leftTree[len(leftTree)-2]+1==root:
        if judgeTree(leftTree,count-1) and judgeTree(rightTree,count-1):
            return True
    elif len(leftTree)==1 and leftTree[0]+1==root:
        return True
    else:
        return False


if input[0][0]==0:
    print("true")
else:
    point = input[0][0]
    wordList = input[1]
    judge = False
    icount = 0
    for i in range(10):
        if point == pow(2,i)-1:
            icount = i
            judge = True
    if not judge:
        print("false")
    else:
        if judgeTree(wordList,icount):
            print("true")
        else:
            print("false")