n = int(input())
result = 0
for i in range(n+1):
    result += str(i).count("1")
print(result)