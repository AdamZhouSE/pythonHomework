length = int(input())
s = input().split('VK')

count = 0
sStr = ''
for i in s:
    if i == '':
        count += 1
    sStr += i

for i in range(len(sStr) - 1):
    if sStr[i] == sStr[i + 1]:
        count += 1
        break

print(count)