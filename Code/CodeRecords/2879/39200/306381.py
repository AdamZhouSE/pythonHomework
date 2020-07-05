n = int(input())
x = []
y = []
result = ""
for i in range(n ** 2):
    p = input().split()
    if p[0] not in x and p[1] not in y:
        x.append(p[0])
        y.append(p[1])
        result += str(i + 1)
        result += " "
print(result[:-1:])
