n = int(input())
tmp = 0
i = 0
while (tmp - n) % 2 == 1 or tmp < n:
    i += 1
    tmp += i
print(i)
