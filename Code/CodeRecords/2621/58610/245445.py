a = eval('[' + input() + ']')
max_sum, max_here = a[0], a[0]
for num in range(1, len(a)):
    if max_here <= 0:
        max_here = a[num]
    else:
        max_here += a[num]
    max_sum = max(max_sum, max_here)
print(max_sum)
