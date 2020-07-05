n = int(input())
s = 0
for i in range(n + 1):
    s += list(str(i)).count("1")
print(s)