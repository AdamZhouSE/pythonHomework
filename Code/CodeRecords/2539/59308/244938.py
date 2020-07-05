a = eval(input())
b = list()
for i in range(1, len(a)):
    if a[i] < a[i-1]:
        b.append(i)

b[0] = b[0]-1

try:
    print(b[1] - b[0] + 1)
except IndexError:
    print(len(a))




