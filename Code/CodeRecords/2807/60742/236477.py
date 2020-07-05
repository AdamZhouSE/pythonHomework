l0 = input().split()
n = int(l0[0])
m = int(l0[1])
a = input().split()
b = input().split()
a_odd = b_odd = a_even = b_even = 0
for i in range(n):
    a[i] = int(a[i])%2
    if a[i]==0:
        a_even += 1
    else:
        a_odd += 1
for i in range(m):
    b[i] = int(b[i])%2
    if b[i]==0:
        b_even += 1
    else:
        b_odd += 1
res = min(a_even,b_odd) + min(a_odd,b_even)
print (res)