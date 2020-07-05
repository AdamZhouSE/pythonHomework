class Solution:
    def bitwiseComplement(self, N: int) -> int:
        b_N = bin(N)
        count = 0
        res = 0
        for i in range(len(b_N)-1, 1, -1):
            if b_N[i] == '0':
                res += 2**count
                count += 1 
            elif b_N[i] == '1':
                count += 1
        return res


if __name__=="__main__":
    s=int(input())
    x=Solution().bitwiseComplement(s)
    print(x)