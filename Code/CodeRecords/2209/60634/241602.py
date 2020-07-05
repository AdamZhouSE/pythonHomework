def march(j, word, target):
    i = 0
    while i < len(word):
        if (j >= len(target)) or (word[i] != target[j]):
            return False
        i += 1
        j += 1
    return True

def fillSpace(index,space,target,words):
    str = target[space[index][0]:space[index][1] + 1]
    i = 0
    while i < len(words):
        j = 0
        while j < len(words[i]):
            if march(j,str,words[i]):
                leftBound = space[index][0]-j
                rightBound = space[index][1]+(len(words[i])-j-len(str))
                if (leftBound >= 0)and(rightBound < len(target)):
                    k = 1
                    while index - k >= 0:
                        if leftBound <= space[index-k][1]:
                            if leftBound<=space[index-k][0]:
                                space.remove(space[index-k])
                            else:
                                space[index-k][1] = leftBound-1
                                break
                        k -= 1
                    k = 1
                    while index + k < len(space):
                        if rightBound >= space[index+k][0]:
                            if leftBound>=space[index+k][1]:
                                space.remove(space[index+k])
                                k -= 1
                            else:
                                space[index+k][0] = rightBound+1
                                break
                        k += 1
                    space.remove(space[index])
                    return 1
            j += 1
        i += 1
    return 0


number = int(input())
target = input()
words = []
cut = 0
# 按从短到长的顺序读取报纸单词
for i in range(number):
    temp = input()
    if len(words) == 0:
        words.append(temp)
    else:
        i = 0
        while i <= len(words):
            if i == len(words):
                words.append(temp)
            if len(temp) <= len(words[i]):
                words.insert(i, temp)
                break
            i += 1
# 从长到短无重叠填补勒索信
space = []  # 记录未填补区段
i = 0
sBegin = -1
sEnd = -1
while i < len(target):
    j = len(words)-1
    while j >= -1:
        if j == -1:
            if sBegin == -1:
                sBegin = i
                sEnd = i
            else:
                sEnd += 1
            break
        if march(i, words[j], target):
            cut += 1
            i += len(words[j]) - 1
            if sBegin != -1:
                space.append([sBegin, sEnd])
                sBegin = -1
                sEnd = -1
            break
        j -= 1
    if (i == len(target) - 1) and (sBegin != -1):
        space.append([sBegin, sEnd])
    i += 1

# 当未填满继续填充
if len(space) == 0:
    print(cut)
else:
    i = 0
    while i < len(space):
        cut += fillSpace(i,space,target,words)
        i += 1
    if len(space) == 0:
        print(cut)
    else:
        fixWords = []
        i = 0
        while i < len(words) - 1:
            j = i + 1
            while j < len(words):
                fixWords.append(words[i]+words[j])
                fixWords.append(words[j]+words[i])
                j += 1
            i += 1
        i = 0
        while i < len(space):
            if fillSpace(i, space, target, fixWords) == 1:
                cut += 2
            i += 1
        if len(space) == 0:
            print(cut)
        else:
            print(target)
            print(words)
            print(-1)
