def connected(words,key):
    judge=0
    for i in range(len(words)):
        if words[i]!=key[i]:
            judge+=1
    if judge==1:
        return True
    else:
        return False
def check(words,key,destination):
    minimum=100
    ret=[]
    for i in words:
        if i==destination and connected(i,key):
            return [1,[[i]]]
        elif connected(i,key):
            tempWords=[]+words
            tempWords.remove(i)
            temp=check(tempWords,i,destination)
            tempNum=1+temp[0]
            if tempNum<minimum:
                minimum=tempNum
                ret=[]
                for j in temp[1]:
                    ret.append([i] + j)
            elif tempNum==minimum:
                for j in temp[1]:
                    ret.append([i] + j)
    return [minimum,ret]
beginWord=input()
endWord=input()
wordList=eval(input())
if endWord not in wordList:
    print('[]')
else:
    temp=check(wordList,beginWord,endWord)
    print(temp[1])