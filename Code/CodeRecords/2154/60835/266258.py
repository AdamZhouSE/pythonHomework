n = input()
result = True
for x in range(len(n)//2+1):
    if n[x] != n[len(n)-x-1]:
        result = False
        break
print(result)