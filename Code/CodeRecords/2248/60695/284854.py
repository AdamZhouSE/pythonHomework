n = int(input())
a = int(input())
b = int(input())
if a < b:
    i = a
else:
    i = b
while n > 0:
    if i % a == 0 or i % b == 0:
        n -= 1
    i += 1
print(int((i-1) % (pow(10, 9) + 7)))