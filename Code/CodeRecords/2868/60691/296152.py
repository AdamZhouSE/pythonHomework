n = int(input())
s = input().split(' ')
l = []
for i in range(len(s)):
    l.append(int(s[i]))

odd = 0
even = 0
for i in range(len(l)):
    if l[i] % 2 == 0:
        even += 1
    else:
        odd += 1

print(min(even, odd))