class Solution:
    def get_count(self, s, t):
        lent = len(t)
        cnt = 0
        for ii in range(0, len(s)-lent+1):
            if s[ii:ii+lent] == t:
                cnt += 1
        return cnt


if __name__ == "__main__":
    try:
        while True:
            N = int(input())
            ty = []
            for i in range(N):
                ty.append(input())
            S = input()
            ans = 0
            count = []
            ss = Solution()
            for i in range(0, N):
                ans = max(ans, ss.get_count(S, ty[i]))
                count.append(ss.get_count(S, ty[i]))
            print(ans)
            for i in range(0, N):
                if count[i] == ans:
                    print(ty[i])
    except EOFError:
        exit()
