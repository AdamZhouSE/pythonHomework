import math

bucket = int(input())
tryTo = int(input())
time = int(input())

section = time // tryTo + 1

num = 0
while True:
    if math.pow(section, num) >= bucket:
        break
    num += 1

print(num)
