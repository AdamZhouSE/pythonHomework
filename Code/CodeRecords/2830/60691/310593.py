s1 = list(map(int, input().split(' ')))
s2 = list(map(int, input().split(' ')))

base = s1[0]
bitlen = s1[1]

count = 0

for i in range(bitlen):
    count += s2[i] * int(pow(base, bitlen-i-1))

if count % 2 == 0:
    print("even")
else:
    print("odd")

