import itertools
import math
s = input()
li = list(s)
combiners = list(itertools.permutations(li))
result = []
for i in combiners:
    result.append(int(''.join(i)))
for i in result:
    if len(str(i)) != len(s):
        result.remove(i)    
for i in range(100):
    if int(math.pow(2,i)) in result:
        print('true')
        quit()

print('false')