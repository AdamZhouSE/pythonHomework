num = int(input())
for i in range(num):
    if i * i == num:
        print(i)
        break
    elif i * i > num:
        print(i - 1)
        break
    else:
        continue