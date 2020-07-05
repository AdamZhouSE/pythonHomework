import math
lst1=input().split()
lst1=list(map(int,lst1))
lst2=input().split()
lst2=list(map(int,lst2))
def val(lst):
    value = 0
    for i, ch in enumerate(lst.reverse()):
        if int(ch) == 1:
            value += int(math.pow(-2, i))
        else:
            continue
    return value
        
value = val(lst1) + val(lst2)
res = []
while value:
    res.append(value % (2))
    value = - (value // 2)
if value==0:
    print([0])
else:
    print(res)