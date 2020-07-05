import math
label=int(input())
res=[label]
while label>1:
    level=int(math.log(label,2))
    start=2**level
    r=(label-start)//2
    label=start-1-r
    res.append(label)
print(res[::-1])
