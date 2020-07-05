import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
root=nums[0]
del(nums[0])
