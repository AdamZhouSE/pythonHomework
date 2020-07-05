import itertools
class Solution(object):
    def reorderedPowerOf2(self, N):
        return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                   for cand in itertools.permutations(str(N)))
    
s=Solution()
if(s.reorderedPowerOf2(int(input()))):
   print("true")
else:
   print("false")


