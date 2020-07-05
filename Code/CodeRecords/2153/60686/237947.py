input_str = input()
num = int(input_str)
if num < 0:
    result = input_str[1:len(input_str)]
    print("-", end="")
    print(result[::-1])
else:
    print(int(input_str[::-1]))
