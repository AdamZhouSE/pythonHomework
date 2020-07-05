src = input()
dest = input()
ns = 0
nd = 0
for i in range(0, len(src)):
    ns = ns * 2 + int(src[i])
for i in range(0, len(dest)):
    nd = nd * 2 + int(dest[i])
# print(ns)
sum = nd + ns
result = bin(sum // 2)
result = result + str(sum % 2)
print(result[2:len(result)])
