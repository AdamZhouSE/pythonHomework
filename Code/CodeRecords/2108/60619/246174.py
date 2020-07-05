n = int(input())
result = 0
for i in range(n+1):
    if str(i).count("1") > 0:
        result += 1
print(result)