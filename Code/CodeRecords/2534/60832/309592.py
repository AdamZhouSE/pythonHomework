import json
from numpy import *
ar=json.loads(input())
ans=array(ar)

ans=[y for x in ans for y in x]
ans.sort()
print(ans)

