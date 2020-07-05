n = int(input())
a = []
for i in range(n):
    for x in eval(input()):
        a.append(int(x))
m = int(input())
res = 'False'
for i in range(len(a)):
    if a[i]==m:
        res = 'True'
        break
print(res)