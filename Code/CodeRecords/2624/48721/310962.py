import re
import operator

class Functiom:
    def diff(self, input):
        items = re.split('(\D)', input)
        nums = list(map(int, items[::2]))
        ops = list(map({'+':operator.add, '-':operator.sub, '*':operator.mul}.get, items[1::2]))
        def calc(low, high):
            if low == high:
                return [nums[low]]
            return [ops[i](a, b)
               for i in range(low, high)
               for a in calc(low, i)
               for b in calc(i + 1, high)]
        return calc(0, len(nums)-1)

a=input()
s=Functiom()
res=s.diff(a)
print(res)
