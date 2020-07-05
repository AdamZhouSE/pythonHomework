class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        return sum(1 for i in range(L,R+1) if bin(i).count('1') in [2,3,5,7,11,13,17,19])
            
if __name__ == '__main__':
    s=Solution()
    n=int(input())
    for i in range(n):
        line=input().split()
        num=list(map(int, line))
        a=s.countPrimeSetBits(num[0], num[1])
        print(a)
