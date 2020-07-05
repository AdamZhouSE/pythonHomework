a=[int(x) for x in input()[1:-1].split(",")]
b=[int(x) for x in input()[1:-1].split(",")]
c=a+b
c.sort()
print(c)