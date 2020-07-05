class Solution:
    def find(self, s):
        slist = list(s)
        sst = list(set(slist))
        re = len(slist)

        for i in range(len(s)-len(sst)): # 从i开始的子串
            right = i+len(sst)-1 # 结尾是right
            while right<len(s):
                isvalid = 1
                tmp = s[i:right+1]
                tmp1 = len(slist)
                for item in sst:
                    if item not in tmp:
                        isvalid = 0
                        break
                if isvalid:
                    tmp1 = min(tmp1,right-i+1)
                    if tmp1==len(sst):
                        print(len(sst))
                        return
                right += 1
            re = min(re,tmp1)
        print(re)
        return


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        data = input()
        s = Solution()
        s.find(data)



