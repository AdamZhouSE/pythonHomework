
class Solution:

    def isSubsequence(self,s, t):

        j=0#j表示t的当前的index，从0处开始搜索

        for i in range(len(s)):#依据s进行搜索

            temp=s[i]#当前需要搜索的字符为temp

            try:

                res=t.index(temp,j)

            except ValueError:#如果没找到返回错误

                return False

            else:#找到了

                j=res+1#从j的下一个开始搜索

        #for循环结束，说明全部找到了

        return True

test = Solution()
s = input()
t = input()
res = test.isSubsequence(s,t)
print(res)