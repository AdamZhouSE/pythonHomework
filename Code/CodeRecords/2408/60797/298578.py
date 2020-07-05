class Solution:
    count = 0

    def isPrime(self, num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return True
            else:
                return False

    def perm(self, n, begin, end):
        if begin >= end:
            s.count +=1
        else:
            i = begin
            for num in range(begin, end):
                if self.isPrime(i) and not self.isPrime(n[num]):
                    continue
                n[num], n[i] = n[i], n[num]
                self.perm(n, begin + 1, end)
                n[num], n[i] = n[i], n[num]

    def find(self, n):
        sq = [i for i in range(1,n+1)]
        self.perm(sq, 0, n)
        return s.count



if __name__ == '__main__':
    n = int(input())
    s = Solution()
    re = s.find(n)
    print(re)