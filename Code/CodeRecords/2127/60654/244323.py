a = int(input())
b = list(input().split(","))
result = 0
for i in b:
    result = (a**int(i)) % 1337
    result *= (a**10) 
    result %= 1337
print(result)
