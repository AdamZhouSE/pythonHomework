rom = {'$': 0, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
target = input() + '$'
result = 0
for i in range(len(target)-1):
    num = rom[target[i]]
    if num < rom[target[i+1]]:
        result -= num
    else:
        result += num
print(result)