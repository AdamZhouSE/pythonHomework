base = 1
result = 0
for c in input()[::-1]:
    result += ((ord(c)-ord('A'))+1)*base
    base *= 26
print(result)