wallHeight = list(map(int, input().split(" ")))[1]
heights = list(map(int, input().split(" ")))
result = 0
for i in heights:
    if i <= wallHeight:
        result += 1
    else:
        result += 2
print(result)