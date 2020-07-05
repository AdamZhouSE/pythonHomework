nums = eval(input())
a,b,c = [],[],[]
for num in nums:
    if num == 0:
        a.append(0)
    elif num == 1:
        b.append(1)
    elif num == 2:
        c.append(2)
result = []
result.extend(a)
result.extend(b)
result.extend(c)
print(result)