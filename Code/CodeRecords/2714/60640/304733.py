import collections


class Solution:

    def longest_dragon(self, arr, start):
        dragon = []
        visited = [0 for _ in range(len(arr))]
        final_res = []
        for i in range(start, len(arr)):
            res = []
            tmp = Solution().dfs(arr, i, dragon, visited, res)
            final_res.append(res)
        return final_res

    def dfs(self, arr, start, dragon, visited, res):
        if visited[start] == 1:
            return dragon
        visited[start] = 1
        dragon.append(arr[start])
        for i in range(start+1, len(arr)):
            if len(arr[i]) == len(arr[start]) + 1 and Solution().match(arr[start], arr[i]):
                tmp = Solution().dfs(arr, i, dragon, visited, res)
            elif len(arr[i]) > len(arr[start]) + 1:
                break
        visited[start] = 0
        is_max = True
        if len(res) < len(dragon):
            res.clear()
            for i in range(len(dragon)):
                res.append(dragon[i])
        dragon.pop()
        return dragon

    def match(self, s1, s2):
        d = {}
        for i in range(len(s1)):
            if s1[i] in d.keys():
                d[s1[i]] += 1
            else:
                d[s1[i]] = 1
        for i in range(len(s2)):
            if s2[i] in d.keys():
                d[s2[i]] -= 1
            else:
                d[s2[i]] = 0
        for key in d:
            if d[key] > 0:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    st = []
    try:
        while True:
            st.append(input())
    except EOFError:
        myST = sorted(st, key=lambda iii: len(iii))
        # print(myST)
        ans = s.longest_dragon(myST, 0)
        # print(ans)
        new_ans = sorted(ans, key=lambda iii: len(iii), reverse=True)
        print(len(new_ans[0]))
        for ii in range(len(new_ans[0])):
            print(new_ans[0][ii])
