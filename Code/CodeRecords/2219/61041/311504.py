import math
c=eval(input())
hi=int(math.sqrt(c))+1
j=0
for a in range(hi):
    b=math.sqrt(c-a*a)
    if int(b)==b:
        j=1
        break
if j==1:print('True')
else:print('False')