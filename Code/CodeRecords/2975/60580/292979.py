l = list(input())
l.sort()
i = 0
result = ""
while i < len(l):
    result = result + l[i]
    i = i + 1
print(result)