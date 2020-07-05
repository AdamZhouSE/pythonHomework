input_array = list(map(int, input()[1:-1].split(",")))
current_max = 0
ans = 0
for i in range(0, len(input_array)):
    current_max = max(input_array[i], current_max)
    if current_max == i:
        ans += 1
print(ans)