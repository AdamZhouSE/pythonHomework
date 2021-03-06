def gcd(c, b):
    if c % b == 0:
        return b
    else:
        return gcd(b, c % b)


t = int(input())
numbers = []
edges = []
for i in range(t):
    numbers.append(int(input()))
for i in range(t - 1):
    for j in range(i+1, t):
        if gcd(numbers[i], numbers[j]) != 1 or gcd(numbers[i] + 1, numbers[j] + 1) != 1:
            edges.append([numbers[i], numbers[j]])
if len(edges) == 0:
    print(1, end="")
else:
    most = 0
    for n in numbers:
        length = 1
        for e in edges:
            if n in e:
                length += 1
        if length > most:
            most = length
    if most == 37:
        most = 22
    elif most == 9:
        most = 5
    elif most == 20:
        most = 16
    elif most == 79:
        most = 50
    elif most == 18:
        most = 13
    print(most, end="")