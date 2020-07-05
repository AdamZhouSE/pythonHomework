import math
source=eval(input())
h=int(input())
for i in range(1,max(source)+1):
    sums=0
    for a in source:
        sums=sums+math.ceil(a/i)
    if(sums<=h):
        print(i)
        break