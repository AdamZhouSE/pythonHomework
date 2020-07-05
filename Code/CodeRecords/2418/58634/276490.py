# 4x+2y = a
# x+y = b
# (a-2b)/2 = x
# 2b -a/2 = y

a = int(input())
b = int(input())
x = (a-2*b)/2
y = 2*b-a/2
if x!=int(x) or y!=int(y) or x<0 or y<0:
    print([])
else:
    print([int(x),int(y)])