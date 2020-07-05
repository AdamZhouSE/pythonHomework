'''
思路 分子分母通分做加法
'''

class Solution:

    def gcd(self, a, b):
        while a != 0:
            a, b = b%a, a
        return b

    def fractionAddition(self, expression: str) -> str:
        s = set()
        i = 0
        l1 = []
        while i < len(expression):
            if i > 0 and expression[i-1] == '/':
                j = i
                while j < len(expression) and ord(expression[j]) >= ord('0') and ord(expression[j]) <= ord('9'):
                    j += 1
                s.add(int(expression[i:j]))
                l1.append(int(expression[i:j]))
                i = j
            else:
                i += 1

        # 求所有分母的最小公倍数
        val1 = 1; gcd_val = 0
        for val2 in s:
            gcd_val = self.gcd(val1, val2)
            val1 = (val1 * val2) // gcd_val

        # 所有分子通分
        if ord(expression[0]) >= ord('0') and ord(expression[0]) <= ord('9'):
            expression = '+' + expression

        i = 0
        l2 = []
        while i < len(expression):
            if i == 0 or expression[i] == '+' or expression[i] == '-':
                j = i+1
                while j < len(expression) and ord(expression[j]) >= ord('0') and ord(expression[j]) <= ord('9'):
                    j += 1

                l2.append(int(expression[i+1: j]) if expression[i] != '-' else -int(expression[i+1: j]))
                i = j
            else:
                i += 1

        sum = 0
        for a, b in zip(l2, l1):
            sum += a * (val1 // b)

        if sum != 0:
            gcd_val = self.gcd(abs(sum), val1)
            #print('{},{}'.format(sum, val1))
            return '' +  str((abs(sum) // gcd_val) * (sum // abs(sum))) + '/' + str(val1 // gcd_val)
        else:
            return '0/1'

        
if __name__=="__main__":
    n=input()
    x=Solution().fractionAddition(n)
    print(x)