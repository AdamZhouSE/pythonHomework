import itertools
import re

class Solution(object):
    def addOperators(self, num, target):
        if num:
            count = len(num)-1
            rnum = num[-1]

            s = "['','+','-','*'],"
            ss = ""
            for c in range(count):
                ss += s

            ls = []  
            for item in itertools.product(*eval(ss[0:-1])):
                zty = ''.join(list(itertools.chain.from_iterable(zip(list(num),item))))+rnum
                if eval(zty) != target or re.match(r".*([\+\-\*]0)\d.*",zty,re.M|re.I):
                    continue
                else:
                    ls.append(zty)
            return ls
        return []
s=input()
tar=int(input())
print (Solution().addOperators(s,tar))