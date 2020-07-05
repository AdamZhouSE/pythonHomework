n = int(input())
a = int(input())
b = int(input())
c = int(input())

i = 0
no = 0
while True:
    i += 1

    if i % a == 0 or i % b == 0 or i % c == 0:
        no += 1
        if no == n:
            break

print(i)
