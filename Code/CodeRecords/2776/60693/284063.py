def findConectedWords(oriwords:[str]):
    words=sorted(oriwords,key=lambda i:len(i)) # 按照单词长度排序，越后面的单词越有可能是连接词
    s=set(words)
    res=[]
    while words:
        word=words.pop(-1)
        s.remove(word)  # s表示单词集，对于每个单词，它不能由自己组成，s剩余的单词长度越来越短
        length=len(word)
        queue=[0]  # queue 表示目前遍历到的单词下标
        while queue:
            q=queue.pop(0)
            flag=False
            for i in range(q+1,length+1):
                if word[q:i] in s:
                    queue.append(i)
                    if i==length:
                        res.append(word)
                        flag:True
                        break
            if flag:break

    res=sorted(res,key=lambda i:oriwords.index(i))
    return res


words=eval(input())
print(findConectedWords(words))
