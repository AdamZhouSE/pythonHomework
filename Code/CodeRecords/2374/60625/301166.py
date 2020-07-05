class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 思路：将字符和其对应的频率保存到一个map中去，对频率进行排序并进行字符串拼接
        count = {}

        s = list(sorted(s))
        while len(s) != 0:
            ct = s.count(s[0])
            count[s[0]] = ct
            s = s[ct:]

        count = sorted(count.items(), key=lambda x: x[1], reverse=True)

        res = ""
        for i in range(len(count)):
            res = res + count[i][1] * count[i][0]

        return res


test=int(input())
for k in range(test):
    n=input()
    nums=input().split(' ')
    solution=Solution()
    res=list(solution.frequencySort("".join(nums)))
    print(" ".join(res)+" ")