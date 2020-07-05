import numpy as np
import re
tree1=list(map(int,re.sub("[null,\[\]]"," ",input()).split()))
tree2=list(map(int,re.sub("[null,\[\]]"," ",input()).split()))
res=list(np.append(tree1,tree2))
res.sort()
res=list(map(int,res))
print(res)