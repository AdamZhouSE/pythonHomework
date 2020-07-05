class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        def check_word(word, pre_dict):
            if len(word) == 0:
                return True
            cur_dict = pre_dict
            for index, c in enumerate(word):
                cur_dict = cur_dict.get(c, None)
                if cur_dict is None:
                    return False
                if cur_dict.get('end', 0) == 1:
                    # 当前字符串前缀与树中单词匹配，递归搜索
                    if check_word(word[index+1:], pre_dict):
                        return True
            return False
        tmp = words.copy()
        words.sort(key=lambda x: len(x))
        ans = []
        pre_dict = {}
        for item in words:
            if len(item) == 0:
                continue
            if check_word(item, pre_dict):
                ans.append(item)
            else:
                # insert word
                cur_dict = pre_dict
                for c in item:
                    if cur_dict.get(c, None) is None:
                        cur_dict[c] = {}
                    cur_dict = cur_dict.get(c)
                cur_dict['end'] = 1
        res = []
        for i in tmp:
            if i in ans:
                res.append(i)
        return res

inputStr = input()
temp = inputStr.replace(" ","").replace("[","").replace("]","").replace('"','').split(",")
print(Solution().findAllConcatenatedWordsInADict(temp))