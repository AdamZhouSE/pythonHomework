a = int(input())
b = input().split(",")
c = "".join(b)
num = int("".join(b))
mul = a
for i in range(num-1):
    a *= mul
result = a%1337
print(result)

