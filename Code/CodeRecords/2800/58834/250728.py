n_and_d = input()
n_and_d_1 = n_and_d.split()
n = int(n_and_d_1[0])
d = int(n_and_d_1[1])
bn_original = input()
bn = bn_original.split()
counts = 0
for b in range(1,n):
    while int(bn[b]) <= int(bn[b-1]):
        bn[b] = d+int(bn[b])
        counts += 1
print(counts)
