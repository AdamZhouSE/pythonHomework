class Solution:
    def find(self, fences, cows):
        re = 0
        cows.sort(key=lambda x: x[0], reverse=True)
        cows.sort(key=lambda x: x[1])
        for i in range(len(cows)):
            if min(fences[cows[i][0] - 1:cows[i][1]]) > 0:
                for j in range(cows[i][0] - 1, cows[i][1]):
                    fences[j] -= 1
                re += 1
        return re
                

if __name__ == '__main__':
    [n, m] = [int(a) for a in input().split()]
    fences = []
    for i in range(n):
        fences.append(int(input()))
    cows = []
    for i in range(m):
        cows.append([int(a) for a in input().split()])
    s = Solution()
    res = s.find(fences, cows)
