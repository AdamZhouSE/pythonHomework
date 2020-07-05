import math
def numOf5(n):
    return int(math.log(n,5))
k = int(input())
var = 1
i = k
while i>0:
    var *= 5
    i -= numOf5(var)
if k==0:
    print(5)
elif i<0:
    print(0)
else:
    print(4*var)