
from collections import defaultdict
from collections import deque
begin=input()
end=input()
wordlist=eval(input())
def func(begin,end,wordlist):
    size,general_dic=len(begin),defaultdict(list)

    #general_dic是一个以每个单词中一个字符被*替换为键，该单词为值初始列表元素
    for w in wordlist:
        for _ in range(size):
            general_dic[w[:_]+"*"+w[_+1:]].append(w)

    #BFS
    queue=deque()
    #其中1是为了区分node所属层
    queue.append((begin,1))
    mark_dic=defaultdict(bool)#bool默认值为false所有不在list中的word
    mark_dic[begin]=True#begin在list中
    #队列非空
    while queue:
        cur_word,level=queue.popleft()
        for i in range(size):
            #寻找有一个字符只差，既键相同
            for neighbour in general_dic[cur_word[:i]+"*"+cur_word[i+1:]]:
                if neighbour==end:return level+1
                if not mark_dic[neighbour]:
                    queue.append((neighbour, level + 1))
                    if(level>len(wordlist)):
                        return 0
    return 0
print(func(begin,end,wordlist))