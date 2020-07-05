import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
listline.sort()
output=""
for i in range(n-1):
    output+=str(listline[i])+" "
output+=str(listline[-1])
print(output)