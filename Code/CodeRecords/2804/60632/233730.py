formula = input()
numbers = sorted(formula[::2])
result = ''
for number in numbers:
    result = result + number + '+'
print(result[:-1])