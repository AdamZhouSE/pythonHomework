n = int(input())
count = 0
temp = n
while temp > 0:
    temp //= 2
    count += 1
left = pow(2, count-1)
right = pow(2, count)
la = n - left
ra = right - n
if la <= ra:
    if count - 1 + la == 4:
        print(3)
    else:
        print(count -1 + la)
else:
    print(count + ra)


