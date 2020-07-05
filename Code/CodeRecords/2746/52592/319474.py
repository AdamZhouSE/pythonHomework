from collections import defaultdict
from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        size, general_dic = len(beginWord), defaultdict(list)
        for w in wordList:
            for _ in range(size):
                general_dic[w[:_]+"*"+w[_+1:]].append(w)
        queue = deque()
        queue.append((beginWord, 1)) 
        mark_dic = defaultdict(bool)  
        mark_dic[beginWord] = True
        while queue:
            cur_word, level = queue.popleft()   
            for i in range(size):              
                for neighbour in general_dic[cur_word[:i]+"*"+cur_word[i+1:]]:
                    if neighbour == endWord: return level + 1
                    if not mark_dic[neighbour]:
                        mark_dic[neighbour] = True
                        queue.append((neighbour, level+1))  
        return 0

m=input();
n=input();
wl=input();
wl=wl.replace('[','');
wl=wl.replace(']','');
wl=wl.replace('"','');
wl2=wl.split(",")
a=Solution()
b=a.ladderLength(m,n,wl2)
print(b)