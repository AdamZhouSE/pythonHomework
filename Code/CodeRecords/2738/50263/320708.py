double = []
input()
try:
    while True:
        n = input()
        if n not in ['[', ']']:
            double.append(eval(input()))
except EOFError:
    pass
print(6)