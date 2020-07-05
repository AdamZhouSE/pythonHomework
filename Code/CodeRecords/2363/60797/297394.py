class Solution:
    def find(self, n):
        bs = bin(n)
        bss = bs[2:]
        tmp = 0
        for i in range(bss):
            if bss[i]=='1':
                continue
            else:
                tmp = tmp+ pow(2,len(bss)-1-i)
        re = tmp
        return re



if __name__ == '__main__':
    n = int(input())
    s = Solution()
    re = s.find(n)
    print(re)