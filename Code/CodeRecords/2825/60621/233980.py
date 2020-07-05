from functools import reduce
a=int(input())
add=lambda x,y:x+y
total=[]
for i in range(a):
    smith = [int(x) for x in input().split()]
    total.append(reduce(add,smith))
smith=total[0]
total.sort(reverse=True)
print(total.index(smith)+1)