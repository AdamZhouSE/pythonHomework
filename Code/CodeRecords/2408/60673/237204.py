import math

inp = int(input())
num_prime = 3;
if (inp == 1):
    res = 1
elif (inp == 2):
    res = 2
elif (inp == 3):
    res = 6
else:
    for i in range(4, inp):
        log = True
        for j in range(2, i):
            if (i % j == 0):
                log = False
                break
        if (log):
            num_prime += 1
    res = (math.factorial(num_prime) * math.factorial(inp - num_prime)) % (pow(10, 9) + 7)
print (res)
