a = int(input())
b = ''.join(('' + input()).split(','))
b = int(b)
t = pow(a,b) % 1337
print(t)