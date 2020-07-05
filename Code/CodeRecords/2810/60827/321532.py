n = input()
b = max([int(x) for x in list(n)])
a = [""] * b
for i in n:
    temp = int(i)
    for j in range(b):
        a[j]+= "1" if temp > 0 else "0"
        temp-=1
print(b)
a = [bin(int(x, 2))[2:] for x in a]
print(" ".join(a))