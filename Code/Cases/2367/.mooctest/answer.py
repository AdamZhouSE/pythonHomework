class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        def function(k):
            if k%2==0 or k%5==0:
                return -1
            else:
                result=1
                mod=1
                while True:
                    mod=mod%k
                    if mod==0:
                        return result
                    else:
                        result+=1
                        mod=mod*10+1
        return function(K)
a = int(input())
s = Solution()
print(s.smallestRepunitDivByK(a))