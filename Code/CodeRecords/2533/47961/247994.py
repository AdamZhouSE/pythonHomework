a=[eval(input()) for i in range(1)]
a.sort(key = lambda x: x % 2)
print(a)