string_input = input()
res = 0
for i in range(len(string_input)):
    res *= 26
    res += ord(string_input[i]) - 64
print(res)
