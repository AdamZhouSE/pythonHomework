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

s=input().split(",")

a=int(s[0])
b=int(s[1])

solution=Solution()
print(solution.combinationSum3(a,b))