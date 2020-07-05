target = abs(int(input()))
k = 0
while target > 0:
    k += 1
    target -= k

if target % 2 == 0:
    print(k)
elif target % 2 == 1:
    print(k + 1)
