class Solution :
    def kobe(self):
        coin = str(input())
        coins = list(coin)
        coins.reverse()
        i = 0
        while coins[i] != '0' :
            i += 1
            if (i == coins.__len__()) :
                return 0
        result = 1
        i += 1
        while i < coins.__len__() :
            if coins[i] != coins[i-1] :
                result += 1
            i += 1
        return result
so = Solution()
print(so.kobe(),end='')