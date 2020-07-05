class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        def gcd(a, b): 
            if (a == 0): 
                return b          
            return gcd(b % a, a) 

        def lcm(a, b): 
            return ((a * b) // gcd(a, b)) 

        def divTermCount(a, b, c, num): 

            return ((num // a) + (num // b) + (num // c) 
                    - (num // lcm(a, b)) 
                    - (num // lcm(b, c)) 
                    - (num // lcm(a, c)) 
                    + (num // lcm(a, lcm(b, c)))) 
        def findNthTerm(a, b, c, n):          
            low = 1
            high = max(a, b, c) * n
            mid = 0

            while (low < high): 
                mid = low + (high - low) // 2

                if (divTermCount(a, b, c, mid) < n): 
                    low = mid + 1

                else: 
                    high = mid 
            return low 
        return findNthTerm(a,b,c,n)
t=int(input())
a=int(input())
b=int(input())
c=int(input())
print(Solution().nthUglyNumber(t,a,b,c))
