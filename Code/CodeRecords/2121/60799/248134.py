(n, pp, res) = min(int(input()), 10),    10,    0
for i in range(n):
    res += pp
    pp *= (10 - i - 1)
print(int(res*9/10)+1)