num = int(input())
flag = False
for i in range(1, num//2+2):
    if i * i == num:
        flag = True
        break
print(flag)
