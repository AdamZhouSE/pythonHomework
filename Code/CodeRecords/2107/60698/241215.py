a = int(input())
b = 1
flag = True
while True:
    if a < b:
        flag = False
        break
    if a == b:
        flag = True
        break
    b = b * 2

print(flag)