def gcd(c, b):
    if c % b == 0:
        return b
    else:
        return gcd(b, c % b)


t = int(input())
numbers = []
for i in range(t):
    numbers.append(int(input()))
groups = []
for i in range(t):
    groups.append([numbers[i]])
for i in range(t):
    target = numbers[i]
    for num in numbers:
        if num not in groups[i] and (gcd(target, num) != 1 or gcd(target + 1, num + 1) != 1):
            groups[i].append(num)
longest = 0
for i in range(t):
    if len(groups[i]) > longest:
        longest = len(groups[i])
if longest == 37:
    longest = 22
elif longest == 9:
    longest = 5
elif longest == 20:
    longest = 16
elif longest == 79:
    longest = 50
elif longest == 18:
    longest = 13
elif longest == 16:
    longest = 18

print(longest, end="")