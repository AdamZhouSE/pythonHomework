import math
def find(a):
    return 2**math.ceil(math.log2(a))
b=int(input())
for i in range(b):
    a=int(input())
    print(find(a))