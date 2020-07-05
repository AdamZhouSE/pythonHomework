class Solution:
    def is_subarray(self, s: str, t: str) -> bool:
        m = len(s)
        cnt = 0
        n = len(t)
        for i in range(n):
            if t[i] == s[cnt]:
                cnt += 1
            if cnt == m:
                return True
        return False


if __name__ == '__main__':
    s = input()
    t = input()
    print(Solution().is_subarray(s, t))