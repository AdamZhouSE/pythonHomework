data = eval(input())
k = int(input())
fractions = []
for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        fractions.append(str(data[i]) + '/' + str(data[j]))
value = [eval(x) for x in fractions]
match = dict(zip(value, fractions))
res = match[sorted(value)[k-1]]
print(list(map(int, res.split('/'))))
