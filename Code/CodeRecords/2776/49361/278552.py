class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        words = set(words)
        if '' in words:
            words.remove('')
        if not words:
            return []
        minl = min(len(i) for i in words)

        def satisfied(w):
            n = len(w)
            if n < minl:
                return False
            if w in words:
                return True
            for i in range(minl, n + 1 - minl):
                if w[:i] in words and satisfied(w[i:]):
                    return True
            return False

        res = []
        for w in words:
            words.remove(w)
            if satisfied(w):
                res.append(w)
            words.add(w)

        return res

inputStr = input()
temp = inputStr.replace(" ","").replace("[","").replace("]","").replace('"','').split(",")
print(Solution().findAllConcatenatedWordsInADict(temp))