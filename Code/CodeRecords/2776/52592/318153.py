class Solution(object):
    def findAllConcatenatedWordsInADict( words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def canBreak(w,wdict):
            if w=='':  flag[0]=True 
            for i in range(len(w)):
                if w[:i+1] in wdict and wdict[w[:i+1]]:
                    canBreak(w[i+1:],wdict)
                    if flag[0]: return True
            
        res=[]
        wdict={}
        for w in words:
            wdict[w]=True 
        for w in words:
            wdict[w]=False
            flag=[False]
            if canBreak(w,wdict):
                res.append(w)
            wdict[w]=True
        return res 
a=eval(input())
print(Solution.findAllConcatenatedWordsInADict(a))