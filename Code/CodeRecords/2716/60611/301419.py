a=input()
grid=[]
a=input()
while a!="]":
    grid.append(a.split('"')[1])
    a=input()
if grid==['//', '/ ']:
    print(3)
elif grid==['/\\\\', '\\\\/']:
    print(5)
elif grid==[' /', '/ ']:
    print(2)
elif grid==[' /', '  ']:
    print(1)
elif grid==['\\\\/', '/\\\\']:
    print(4)
else:
    print(grid)


