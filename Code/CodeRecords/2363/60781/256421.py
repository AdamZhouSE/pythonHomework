
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if 0==N:
            return 1
        res=0
        now=1
        while N:
            if 0==N%2:
                res+=now
            now<<=1
            N>>=1        
        return res
