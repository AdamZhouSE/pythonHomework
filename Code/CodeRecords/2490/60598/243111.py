A = set(map(int, input()[1:-1].split(",")))
B = set(map(int, input()[1:-1].split(",")))
print(sorted(list(A & B)))