a = "".join(input().split("["))
a = "".join(a.split("]"))
a = list(map(int,a.split(",")))
b = "".join(input().split("["))
b = "".join(b.split("]"))
b = list(map(int,b.split(",")))
c = [i for i in a if i in b]
c.sort()
print(c)

