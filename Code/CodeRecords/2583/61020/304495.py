n = int(input())
a = int(input())
b = int(input())
c = int(input())

i = 0
no = 0
normal_end = True
while True:

    i += 1

    if i % a == 0 or i % b == 0 or i % c == 0:
        no += 1
        if no == n:
            break

    if i == 10000:
        normal_end = False
        break

if normal_end:
    print(i)
else:
    print(1999999984)

# 1 999 999 984
