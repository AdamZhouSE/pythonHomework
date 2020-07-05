a = list(input())
res = 0
for i in a:
    res = res*26+ord(i)-64
print(res)