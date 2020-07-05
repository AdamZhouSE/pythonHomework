class Solution:
    def check(self,word1,word2):
        for i in word1:
            if i in word2:
                return False
        return True
    
    def maxProduct(self, words):
        res = 0
        length = len(words)
        for i in range(length):
            for j in range(i,length):
                if self.check(words[i],words[j]):
                    res = max(res, len(words[i])*len(words[j]))
        
        return res

    
s=input();
s=s.replace("[","")
s=s.replace("]","")
s=s.replace('"','')
a=s.split(',')
ss=Solution()
res=ss.maxProduct(a)
print(res)