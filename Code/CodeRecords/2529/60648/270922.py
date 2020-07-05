from collections import Counter
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        return Counter(str(N)) in [Counter(str(1 << i)) for i in range(32)]


if __name__=="__main__":
    s=int(input())
    x=Solution().reorderedPowerOf2(s)
    print(x)