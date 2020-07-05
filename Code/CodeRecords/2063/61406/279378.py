a = input()
b = reversed(a)
result=""
for i in b:
    result += i
print(result==a)