class Solution:
    def minCostToMoveChips(self, chips) -> int:
        even = 0
        for c in chips:
            if c&1==0:
                even+=1
        return min(even,len(chips)-even)


if __name__=="__main__":
    s=input().split(',')
    s=[int(s[i]) for i in range(len(s))]
    x=Solution().minCostToMoveChips(s)
    print(x)