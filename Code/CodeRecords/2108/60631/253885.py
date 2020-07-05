a = int(input())
data = []
for i in range(a+1):
    data.append(str(i))
co = 0
for j in data:
    for k in j:
        if k=='1':
            co = co+1
print(co)