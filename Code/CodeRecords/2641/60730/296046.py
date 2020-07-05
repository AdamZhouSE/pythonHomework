class Solution(object):
    def checkInclusion(self, s1, s2):
        length = len(s1)
        for i in range(len(s2)-length+1):
            if list(sorted(list(s1))) ==list(sorted(list(s2)[i:i+length])):
                return True
        return False


if __name__ == "__main__":
    m = input()
    n = input()
    solution = Solution()
    result = solution.checkInclusion(m, n)
    print(result)
