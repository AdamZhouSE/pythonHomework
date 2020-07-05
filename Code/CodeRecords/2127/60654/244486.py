a = int(input())
b = list(input().split(","))
result = 0
for i in b:
    result += int(i)
    if i != b[b.__len__()-1]:
        result *= 10
print((a**result)%1337)
