import math
lst1=input().split(',')
lst1=list(map(int,lst1))
lst2=input().split(',')
lst2=list(map(int,lst2))
def val(lst):
    value = 0
    i=0
    for x in lst:
        if x == 1:
            value += int(math.pow(-2, i))
        i+=1
    return value

lst1.reverse()
lst2.reverse()
value = val(lst1) + val(lst2)
res = []
while value:
    res.append(value % (2))
    value = - (value // 2)
res.reverse()
print(res)
