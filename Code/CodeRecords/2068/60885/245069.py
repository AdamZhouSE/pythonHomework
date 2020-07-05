x = int(input())
y = int(input())
neg = x < 0 and y >= 0 or x >= 0 and y < 0
if x < 0:
    x = -x
if y < 0:
    y = -y
result = 0
while x > y:
    result += 1
    x -= y
if neg:
    result = -result
print(result)