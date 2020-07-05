import re
import itertools
from bisect import bisect_left

pattern = re.compile('-*[0-9]+')
A = [int(x) for x in pattern.findall(input())]
B = [int(x) for x in pattern.findall(input())]
C = [int(x) for x in pattern.findall(input())]
D = [int(x) for x in pattern.findall(input())]
A_B = [x+y for x, y in itertools.product(A, B)]
C_D = [x+y for x, y in itertools.product(C, D)]
count = 0
for i in A_B:
    j = 0 - i
    for k in C_D:
        if k == j:
            count += 1
print(count)



