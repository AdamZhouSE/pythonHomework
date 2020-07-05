n, d = input().split(' ')
n = int(n)
d = int(d)

f = [1]
for i in range(1, d+1):
    f.append((f[i-1]**n)+1)
print(f[d]-f[d-1])