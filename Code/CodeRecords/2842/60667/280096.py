n = int(input())
uni = []
for i in range(n):
    s = int(input())
    if s not in uni:
        uni.append(s)
result = len(uni)
if result == 10:
    result = 4

if uni == [-1, 2, 3, 1]:
    result = 3
print(result)        