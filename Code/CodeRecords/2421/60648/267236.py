class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace('6','9',1))


if __name__=="__main__":
    s=int(input())
    x=Solution().maximum69Number(s)
    print(x)