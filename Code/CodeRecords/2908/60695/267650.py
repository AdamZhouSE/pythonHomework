n = int(input())
result = []

for i in range(0, n):
    a = input()
    a = a.replace(" ","")
    result.append(sorted(a))
i = 0
result = sorted(result)
while i < len(result)-1:
    if result[i] == result[i+1]:
        result.remove(result[i+1])
    else:
        i += 1

print(len(result), end="")

    