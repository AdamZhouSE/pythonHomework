
class Solution:
    def baseNeg2(self, N: int) -> str:
        if 0==N:
            return "0"
        res=""
        count=0
        while N:
            tmp=N%2
            res+=str(tmp)
            if 1==count%2:
                N+=tmp
            N//=2
            count+=1
        res=list(res)
        res=res[::-1]
        return "".join(res)

n=int(input())
t=Solution()
print(t.baseNeg2(n))