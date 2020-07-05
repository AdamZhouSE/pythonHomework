n = int(input())
s = input().split(' ')
l = []
for i in range(len(s)):
    l.append(int(s[i]))

sum = 0
for i in range(len(l)):
    sum += l[i]

count = 0
for i in range(len(l)):
    temp = sum
    temp -= l[i]
    if temp % 2 == 0:
        count += 1

print(count)