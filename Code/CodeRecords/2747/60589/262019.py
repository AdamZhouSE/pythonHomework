from collections import defaultdict


def findWord(beginWord, endWord, wordList):

    if endWord not in wordList:
        print([])
        return

    L = len(beginWord)

    #生成邻接表
    all_combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(L):
            all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

    routes=[]
    current_word=beginWord
    min_len=len(wordList)+2

    def dfs(current_word,route):
        for i in range(L):
            intermediate_word = current_word[:i] + "*" + current_word[i + 1:]
            for word in all_combo_dict[intermediate_word]:
                copy_route = route[:]
                copy_route.append(word)
                if len(copy_route)<=min_len:
                    if word==endWord:
                        routes.append(copy_route)
                        return
                    dfs(word,copy_route)


    dfs(beginWord,[beginWord,])
    routes.sort(key=lambda x:len(x))
    length=len(routes[0])
    routes=list(filter(lambda x:len(x)==length,routes))
    print(routes)


beginWord=input()
endWord=input()
wordList=eval(input())
findWord(beginWord,endWord,wordList)