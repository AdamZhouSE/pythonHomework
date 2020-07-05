input()
temp = list(map(int,input().split(" ")))
result = 0
for m in temp:
    if(m > 0):
        result += m
    else:
        result -= m
print(result)