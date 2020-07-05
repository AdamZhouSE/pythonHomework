a = {int(i) for i in input()[1:-1].split(',')}
b = {int(i) for i in input()[1:-1].split(',')}
print(sorted(a & b))