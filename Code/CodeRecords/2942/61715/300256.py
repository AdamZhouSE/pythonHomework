class Solution :
    def kobe(self):
        n = int(input())
        numbers = list(map(str, input().split(" ")))
        numbers.sort()
        numbers.reverse()
        number = "".join(numbers)
        print(number,end='')
so = Solution()
so.kobe()