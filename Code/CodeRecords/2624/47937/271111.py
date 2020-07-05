class Solution():
    def diffWaysToCompute(self,x):
        # 递归 + 备忘录
        self.formula = x
        self.memo = {}
        return self._diffWaysToCompute(0, len(x))

    def _diffWaysToCompute(self, lo, hi):
        if self.formula[lo:hi].isdigit():
            return [int(self.formula[lo:hi])]
        if((lo, hi) in self.memo):
            return self.memo.get((lo, hi))
        ret = []
        for i, char in enumerate(self.formula[lo:hi]):
            if char in ['+', '-', '*']:
                leftResult = self._diffWaysToCompute(lo, i + lo)
                rightResult = self._diffWaysToCompute(lo + i + 1, hi)
                ret.extend([eval(str(i) + char + str(j)) for i in leftResult for j in rightResult])
                self.memo[(lo, hi)] = ret
        return ret
    
a=input()
a=str(a)
#x=[2,0]
solution=Solution()
print(solution.diffWaysToCompute(x=a))
