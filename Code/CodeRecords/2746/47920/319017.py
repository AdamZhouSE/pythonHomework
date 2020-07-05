from typing import List
import collections
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return []
        
        L = len(beginWord)
        
        # 表明dict中元素是list type
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i]+"*"+word[i+1:]].append(word)
        
        # Queue for BFS
        queue = [(beginWord, [beginWord], 1)]
        visited = {beginWord: 1}

        ans_list = []
        firstFound = True
        min_length = 0

        while queue:
            curr_word, curr_path, level = queue.pop(0)
            for i in range(L):
                intermediate_word = curr_word[:i] + "*" + curr_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        if firstFound:
                            min_length = level + 1
                            firstFound = False
                            ans_list.append(curr_path+[word])
                        else:
                            if level+1 > min_length:
                                return ans_list
                            else:
                                ans_list.append(curr_path+[word])
                        continue
                    
                    if word in visited and visited[word] < level+1:
                        continue
                    else:
                        visited[word] = level+1
                        queue.append((word, curr_path+[word], level + 1))
        return ans_list

begin = input()
end = input()
inp = eval(input())
s = Solution()
print(len(s.findLadders(begin,end,inp)[0]))



