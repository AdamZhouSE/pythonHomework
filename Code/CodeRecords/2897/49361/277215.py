class Solution(object):
    def maxProduct(self, words):
        words = sorted(words, key=lambda x: -len(x))
        from collections import Counter
        dic = [Counter(item) for item in words]
        res = 0
        l = len(words)
        for i in range(l - 1):
            for j in range(i + 1, l):
                flag = 0
                for char in words[i]:
                    if char in dic[j]:
                        flag = 1
                        break
                if flag == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res


inputStr = input()
strs = inputStr.replace("[", "").replace("]", "").replace('"','').split(",")
print(Solution().maxProduct(strs))