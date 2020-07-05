tem = input().split('"')
letters = []
for n in range(len(tem)):
    if n%2==1:
        letters.append(tem[n])
target = input()
result = ''
for n in letters:
    if target < n:
        result = n
        break
if result == '':
    result = letters[0]
print(result)