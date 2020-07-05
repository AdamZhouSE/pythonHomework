import sys
import re
s=sys.stdin.read()
stack=[]
isTrue=1
for i in s:
    if i=='(':
        stack.append(i)
    elif i==')':
        if len(stack)<1:
            isTrue==0
            break
        else:
            del(stack[-1])
    else:
        pass
if len(stack)!=0:
    isTrue=0
if isTrue==0:
    print("NO")
else:
    print("YES")
    