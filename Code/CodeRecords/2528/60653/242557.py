import re;
#from itertools import *
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
s.sort()
print(s)