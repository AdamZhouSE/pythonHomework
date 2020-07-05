n = int(input())
strSet = set()
for i in range(n):
    item = ''.join(sorted(input())).strip()
    strSet.add(item)
print(len(strSet), end='')
