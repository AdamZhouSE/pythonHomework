a = input()
b = input().split()
i = 0
l = []
oddL = []
result = 0
while i < len(b):
    l.append(int(b[i]))
    i += 1
for val in l:
    if val % 2 == 0:
        result = result + val
    else:
        oddL.append(val)
if len(oddL) % 2 == 0:
    for val in oddL:
        result = result + val;
else:
    oddL.sort()
    j = len(oddL) - 1
    while j != 0:
        result = result + oddL[j]
        j -= 1
print(result)