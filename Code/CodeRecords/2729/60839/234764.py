p = input()
z = p[1:(len(p)-1)]
x = list(map(int,z.split(",")))
y = []

for i in range(0,len(x)):
    if not(x[i] in y):
        y.append(x[i])
    else:
        y.remove(x[i])

print (y[0])