inp = input()
my_arr = []
i = 0
while i < len(inp):
    if inp[i] == '-' or str.isnumeric(inp[i]):
        end_i = i + 1
        while end_i < len(inp):
            if str.isnumeric(inp[end_i]):
                end_i += 1
            else:
                break
        my_arr.append(int(inp[i:end_i]))
        i = end_i
    else:
        i += 1
my_arr.sort()
print(my_arr)
