# LeetCode 241
class Solution:
    def diffWaysToCompute(self, input):
        res = []
        ops = {'+':lambda x,y:x+y, '-':lambda x,y:x-y, '*':lambda x,y:x*y}
        for indx in range(1,len(input)-1):
            if input[indx] in ops.keys():
                for left in self.diffWaysToCompute(input[:indx]):
                    for right in self.diffWaysToCompute(input[indx+1:]):
                        res.append(ops[input[indx]](left,right))                      
        if not res:
            res.append(int(input))
        return res


exp = input()
s = Solution()
print(s.diffWaysToCompute(exp))