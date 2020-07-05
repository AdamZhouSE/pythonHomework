class Solution:
    def find(self, a, b):
        if len(a)!=len(b):
            return 1 # 长度不等
        n = len(a)
        al = a.lower()
        bl = b.lower()
        mode = 0
        is2 = 1 # 完全一样
        is3 = 1 # 不区分大小写一样
        is4 = 1 # 不一样
        for i in range(n):
            if a[i]!=b[i]:
                is2 = 0
            if al[i] != bl[i]:
                return 4
        if is2:
            return 2
        return 3


if __name__ == '__main__':
    a = input()
    b = input()
    s = Solution()
    re = s.find(a, b)
    print(re)
