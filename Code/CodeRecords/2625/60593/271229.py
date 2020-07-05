class Solution(object):
    def addOperators(self, s, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        n = len(s)
        ans = []
        if s == "":
            return []

        def solve(now, i, v, prev, last):
            if i == n:
                # if eval(now)!=v:
                #     print now,v
                if v == target:
                    ans.append(now)
                return
            # add
            solve(now + "+" + s[i], i + 1, v + int(s[i]), int(s[i]), int(s[i]))
            # sub
            solve(now + "-" + s[i], i + 1, v - int(s[i]), -int(s[i]), int(s[i]))
            # multi
            solve(now + "*" + s[i], i + 1, v - prev + prev * int(s[i]), prev * int(s[i]), int(s[i]))
            # space
            if last!=0:
                solve(now + s[i], i + 1, v + 9 * prev + int(s[i])*prev/last, 10 * prev + int(s[i]) *prev/last, last*10+int(s[i]))

        solve(s[0], 1, int(s[0]), int(s[0]), 1)
        if('00' in ans):
            ans.remove('00')
        return ans

s=input()
tar=int(input())
print (Solution().addOperators(s,tar))