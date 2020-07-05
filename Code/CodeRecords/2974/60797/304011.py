class Solution:
    def isPalindrome(self, data):
        for i in range(len(data)):
            if data[i] != data[len(data) - 1 - i]:
                return False
            if i == len(data) - i - 1:
                break
        return True

    def find(self, data):
        re = 0
        for cut in range(1, len(data)):
            A = 0
            B = 0
            for i in range(cut):
                for j in range(i, cut):
                    if len(data[i:j + 1]) % 2 == 1 and self.isPalindrome(data[i:j + 1]):
                        A += 1
            for i in range(cut, len(data)):
                for j in range(i, len(data)):
                    if len(data[i:j + 1]) % 2 == 1 and self.isPalindrome(data[i:j + 1]):
                        continue
                    B += 1
            re = max(re, A * B)
        return re


if __name__ == '__main__':
    n = int(input())
    data = input()
    s = Solution()
    res = s.find(data)
    print(res)
