
class Solution :
    def judge(self,n):
        while n > 0 :
            if n % 10 == 0 :
                return 0
            n /= 10
        return 1
    def serch(self):
        N = int(input())
        i = 1
        while i <= N / 2 :
            if Solution.judge(self, i) == 1 and Solution.judge(self, N - i) == 1 :
                print('['+str(i)+', '+str(N-i)+']')
                return 0
            i += 1
solution = Solution()
solution.serch()
