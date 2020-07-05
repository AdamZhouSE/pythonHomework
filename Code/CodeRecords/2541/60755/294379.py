n = int(input())
all = input()[2:-2].split("],[")
a = []
for i in all:
    a.append(i.split(","))
res = []
num = []
for i in len(a):
    for k in len(a[i]):
        if res.count(a[i][k])==0:
            num.append(a[i][k])
while len(num)!=0