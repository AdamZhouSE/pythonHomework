input = input().split(',')
a = max(input)
input.remove(a)
b = max(input)
input.remove(b)
c = max(input)
input.remove(c)
print(int(a) * int(b) * int(c))