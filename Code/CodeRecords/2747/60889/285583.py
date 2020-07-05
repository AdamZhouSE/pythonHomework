def canChange(str1,str2):
    difLoc = 0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            difLoc = difLoc + 1
            if difLoc == 2:
                return False
    return True

def findWays(endWord,nowWord,wordlist,theWay,ways,shortestway):
    if canChange(nowWord,endWord):
        theWay.append(endWord)
        ways.append(theWay)
        return len(theWay)
    else:
        if len(wordlist) == 0:
            return -1
        for i in wordlist:
            if canChange(nowWord,i):
                newWordlist = wordlist.copy()
                newWordlist.remove(i)
                newWay = theWay.copy()
                newWay.append(i)
                length = findWays(endWord,i,newWordlist,newWay,ways,shortestway+1)
                if length<shortestway and length!= -1:
                    shortestway = length
        return shortestway

beginWord = input()
endWord = input()
wordlist = input().strip("[\"]").split("\",\"")
if wordlist.count(endWord)==0:
    print("[]")
else:
    length = len(wordlist)
    ways = []
    length = findWays(endWord,beginWord,wordlist,[beginWord],ways,length+1)
    i = 0
    while i < len(ways):
        if len(ways[i])>length:
            ways.pop(i)
            i = i - 1
        i = i + 1
    print(ways)
        


















