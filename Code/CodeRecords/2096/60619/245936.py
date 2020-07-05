x = int(input())
result = 0
while result*result < x:
    result += 1
if result**2 > x:
    result -= 1
print(result)