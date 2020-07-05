string1 = input().split()
n = int(string1[0])
k = int(string1[1])
ai = input().split()
result = []
for x in ai:
    if k % int(x) == 0:
        result.append(k // int(x))
print(min(result))

