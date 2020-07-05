class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N = len(s)
        i = 0
        j = 0
        res = ''
        min_val = N
        match = 0
        dic_t = {}
        dic_windows = {}
        for c in t:
            dic_t[c] = dic_t.get(c, 0) + 1

        match_N = len(dic_t)
        while j < N:
            if s[j] in dic_t:
                dic_windows[s[j]] = dic_windows.get(s[j], 0) + 1
                if dic_windows[s[j]] == dic_t[s[j]]:
                    match += 1
                while match == match_N:
                    this_time_val = j - i
                    if min_val > this_time_val:
                        res = s[i:j + 1]
                        min_val = this_time_val

                    if s[i] in dic_t:
                        dic_windows[s[i]] = dic_windows[s[i]] - 1
                        if dic_windows[s[i]] < dic_t[s[i]]:
                            match -= 1
                    i += 1
            j += 1
        return res


if __name__ == "__main__":
    S = input()
    T = input()
    s = Solution()
    ans = s.minWindow(S, T)
    print(ans)
