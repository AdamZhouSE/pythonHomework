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
    for num in numbers:
        if num not in groups[i]:
            judge = True
            for temp in groups[i]:
                if gcd(temp, num) == 1 and gcd(temp+1, num+1) == 1:
                    judge = False
            if judge:
                groups[i].append(num)
longest = 0
for i in range(t):
    if len(groups[i]) > longest:
        longest = len(groups[i])

print(longest, end="")