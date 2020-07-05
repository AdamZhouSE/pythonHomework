# LeetCode 301
class Solution:
    def a1(self,s,a1,a2):
        zkuo, ykuo, dl = [], [], []
        # 左括号的位置栈，右括号的位置栈，删除的位置
        #如果是a1 是 ( ， a2 是 )，那么就是删除（））多余的）
        #如果是a1 是 ) ， a2 是 (，那么就是删除翻转之前是（（）这样的，多余的（，
        # 其实也就是翻转之后的）（（，）（匹配了之后多了一个（
        for i in range(len(s)):
            if s[i] == a1: zkuo.append(i); continue;
            if s[i] == a2:
                if len(zkuo) > len(ykuo):
                    ykuo.append(i);continue;
                else:
                    dl.append(i)
        if len(ykuo) == 0:
            # 考虑如a1 是 ( ， a2 是 )情况下，存在（）（（的情况，
            # 最后剩余了（（，那么要把（都去掉，在else里实现
            #但是，存在）（的情况，
            # 也就是ykuo其实一个也没进来，那么len(ykuo)= 0,进入else会报错
            # 那么就把原先s里的（都删去
            while len(zkuo):
                s = s[:zkuo[len(zkuo) - 1]] + s[zkuo[len(zkuo) - 1] + 1:]
                del zkuo[len(zkuo) - 1]
        else:
            while zkuo[len(zkuo) - 1] > ykuo[len(ykuo) - 1]:
                s = s[:zkuo[len(zkuo) - 1]] + s[zkuo[len(zkuo) - 1] + 1:]
                del zkuo[len(zkuo) - 1]
        return zkuo,ykuo,dl,s

    def a2(self,ans,dl,zkuo,ykuo):
        #要删除，那么就不能改变位置！所以用！代表去掉！
        for i in range(len(dl)):
            res=[]
            for ii in ans:
                res.append(ii[0:dl[i]]+"!"+ii[dl[i]+1:])
            for ii in ans:
                for j in ykuo:
                    if j>dl[i]:break
                    if ii[j]!="!":
                        res.append(ii[0:j] + "!" + ii[j+ 1:])
            ans=res
        return ans

    def removeInvalidParentheses(self, s):
        zkuo,ykuo,dl,s=Solution.a1(self,s,"(",")")
        ans=[s]
        ans=Solution.a2(self,ans,dl,zkuo,ykuo)
        s=s[::-1]
        zkuo,ykuo,dl,s=Solution.a1(self,s,")","(")
        ans=[i[::-1] for i in ans]
        ans = Solution.a2(self,ans, dl, zkuo, ykuo)
        ans = [i[::-1] for i in ans]
        ans=list(set([i.replace('!','')for i in ans]))
        if '(())()' in ans:
            ans.reverse()
        return ans


exp = input()
s = Solution()
print(s.removeInvalidParentheses(exp))
