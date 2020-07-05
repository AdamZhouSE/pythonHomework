from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def helper(count,i,tmp,target):
            #print(count,i,tmp,target)
            if(count==k):
                if(target==0):
                    res.append(tmp)
                return
            for j in range(i,10):
                if(j>target):
                    break
                helper(count+1,j+1,tmp+[j],target-j)
        helper(0,1,[],n)
        return res

s=Solution()
line=eval('['+input()+']')
print(s.combinationSum3(line[0],line[1]))