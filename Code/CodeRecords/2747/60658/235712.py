startword  = input()
endword = input()
wordlist = input()
wordlist = wordlist.replace('["',"")
wordlist = wordlist.replace('"]',"")
wordlist = wordlist.split('","')
que = [[startword]]
alphbet = "abcdefghijklmnopqrstuvwxyz"
flag = False
visited = set(startword)
res = []
if endword not in wordlist:
    print([])
else:
    while (not len(que)==0) and not flag:
        size = len(que)
        subVisited = set()
        for i in range(size):
            path = que.pop(0)
            # print(path)
            word = list(path[-1])
            # print("get last word = "+str(word))
            for j in range(len(word)):
                temp = word[j]
                for k in alphbet:
                    word[j]=k
                    if temp==k:
                        continue
                    newword = "".join(word)
                    if newword in wordlist and newword not in visited:
                        newpath = path.copy()
                        newpath.append(newword)
                        # print("new path is : "+str(newpath))
                        if newword==endword:
                            flag=True
                            res.append(newpath)
                        que.append(newpath)
                        # print("new que is : "+str(que))
                        subVisited.add(newword)
                word[j]=temp
        visited.update(subVisited)
    print(res)    
