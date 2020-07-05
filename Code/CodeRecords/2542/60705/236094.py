input_array = list(map(int, input()[1:-1].split(",")))
num_set = set(input_array)

max_consecutive_length = 1
for num in num_set:
    current_consecutive_length = 1
    while num + 1 in num_set:
        current_consecutive_length += 1
        num += 1
    if current_consecutive_length > max_consecutive_length:
        max_consecutive_length = current_consecutive_length
print(max_consecutive_length)
