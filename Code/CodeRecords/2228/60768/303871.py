target = int(input())
n = 1
i = 2
while n < target:
    n += i
    i += 1
if (n - target) % 2 != 0:
    while (n - target) % 2 == 1:
        n += i
        i += 1
    
print(i - 1)