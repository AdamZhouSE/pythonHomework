num = int(input())
result = False
for n in range(num//2 + 1):
    if n**2 == num:
        result = True
print(result)