string = input()
string = string[1:-1]
m, n = map(int, string.split(","))
for i in range(m, n):
    n = n & i
print(n)
