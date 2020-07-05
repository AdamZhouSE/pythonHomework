from functools import reduce
a=int(input())
b=reduce(lambda x,y:x+y,[int(x) for x in input().split()])
c=[int(x) for x in input().split()]
c.sort()
if a<=2:
    print("YES")
elif(c[a-1]+c[a-2]>=b):
    print("YES")
else:
    print("NO")