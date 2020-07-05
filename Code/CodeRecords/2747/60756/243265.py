from collections import defaultdict
beginWord=input()
endWord=input()
dictionary=input()[2:-2].split('","')
if endWord not in dictionary:
    print("[]")
else:
    ans=[]
    ansMinLength=float("inf")
    L=len(beginWord)
    path_dict=defaultdict(list)
    for word in dictionary:
        for i in range(L):
            path_dict[word[:i]+"*"+word[i+1:]].append(word)
    searchQuene=[(beginWord,[beginWord])]
    visitedMediate=[[beginWord]]
    while searchQuene:
        currentWord,path=searchQuene.pop(0)
        for i in range(L):
            intermediateWord=currentWord[:i]+"*"+currentWord[i+1:]
            for word in path_dict[intermediateWord]:
                currentPath=path[:]
                if word not in path :
                    if len(currentPath)<ansMinLength:
                        currentPath.append(word)
                        if word==endWord:
                            ans.append(currentPath)
                            if len(currentPath)<ansMinLength:
                                ansMinLength=len(currentPath)
                        elif len(currentPath)!=ansMinLength:
                            searchQuene.append((word,currentPath))
    print(ans)