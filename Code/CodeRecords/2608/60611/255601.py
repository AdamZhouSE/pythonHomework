nums = int(input())
resource=[]
for i in range(nums):
    resource.append(input())


def isYuanYinorNot(str):
    if str == "a" or str == "e" or str == "i" or str == "o" or str == "u":
        return 1
    else:
        return 0


def CharacterNumber(str):
    charNumber = []
    for j in range(len(str)):
        if isYuanYinorNot(str[j]) == 0:
            charNumber.append(1)  # 辅音备注1
        else:
            charNumber.append(0)  # 元音备注0
    return charNumber


def subCharacter(str):
    subChar = []
    length = len(str)
    sum = pow(2, length - 2)
    for i in range(sum):
        s = str[-1]
        n = i
        for j in range(length - 2):
            if n % 2 != 0:
                s = str[length - 2 - j] + s
            else:
                pass
            n = n // 2
        s = str[0] + s
        subChar.append(s)
    return subChar


for i in range(nums):
    source = resource[i]
    cNumber = CharacterNumber(source)
    result = []
    if cNumber == sorted(cNumber,reverse=True):
        print(-1)
        continue
    while cNumber[0] == 1:
        cNumber = cNumber[1:]
        source = source[1:]
    while cNumber[-1] == 0:
        cNumber = cNumber[:-1]
        source = source[:-1]
    for j in range(len(source)):
        if cNumber[j] == 0:
            for k in range(j + 1, len(source)):
                if cNumber[k] == 1:
                    result.extend(subCharacter(source[j:k + 1]))
    result=set(result)
    result=sorted(result)
    for j in range(len(result)):
        if j==len(result)-1:
            print(result[-1])
        else:
            print(result[j], end=" ")