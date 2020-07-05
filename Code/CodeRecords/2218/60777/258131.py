temp=[int(x) for x in input().split(',')]
x=max(temp)
temp.remove(x)
y=max(temp)
temp.remove(y)
z=max(temp)
temp.remove(z)

print(x*y*z)