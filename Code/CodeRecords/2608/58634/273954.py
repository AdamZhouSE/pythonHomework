# dfs+递归实现
def cal(str_,res):
    starters = []
    for i in range(len(str_)):
        if isVowel(str_[i]):
            starters.append(str(i))
    def dsearch(subStr,str_):
        if isVowel(str_[int(subStr[0])]) and (not isVowel(str_[int(subStr[-1])])):
            addSub(subStr, str_, res)
        for i in range(int(subStr[-1])+1,len(str_)):
            dsearch(subStr+str(i),str_)
    for i in starters:
        dsearch(i,str_)


def addSub(subStr, str_,res):
    temp = ""
    for i in subStr:
        temp += str_[int(i)]
    res.append(temp)


def isVowel(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char=='u':
        return True
    else:
        return False


t = int(input())
for i in range(t):
    res = []
    cal(input(),res)
    if res == []:
        print(-1)
    else:
        temp = []
        for i in res:
            if not i in temp:
                temp.append(i)
        for i in range(len(temp)):
            if i == len(temp)-1:
                print(temp[i])
            else:
                print(temp[i],end=" ")

