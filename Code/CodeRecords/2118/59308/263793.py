res = list()
for i in range(1000):
    res.append(pow(3, i))

n = int(input())
if n in res:
    print(True)
else:
    print(False)

