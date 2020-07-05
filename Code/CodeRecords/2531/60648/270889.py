from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(i * j for i,j in Counter(s).most_common())


if __name__=="__main__":
    s=input()
    x=Solution().frequencySort(s)
    print(x)