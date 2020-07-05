target = abs(int(input()))
add_sum = 0
k = 0
while add_sum < target:
    k += 1
    add_sum += k
delta = add_sum - target
if delta % 2:
    print(k + 1 + k % 2)
else:
    print(k)
