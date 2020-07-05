import numpy as np
inp =eval(input())
n = int(input())
#print(n)
li =list(inp)
li.sort()
li2 = np.unique(li)
#print(li2)
print(li2[len(li2)-n])