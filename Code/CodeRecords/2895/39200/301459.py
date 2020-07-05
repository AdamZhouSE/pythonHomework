a = input()
m = int(a[1:-1:1].split(",")[0])
n = int(a[1:-1:1].split(",")[1])
result = m
for x in range(m,n+1):
    result = result & x
print(result)
